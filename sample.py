import json
import logging
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
TABLE_NAME = "eqa-validation-results-table"
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
# ---------------------------------------------------------------------------
# FUNCTION 1 — Validator Lambda Input
# ---------------------------------------------------------------------------

def extract_lambda_input(event: dict) -> tuple[str, str, dict]:
 
    # --- format A: SNS-triggered invocation -----------------------------------
    if "Records" in event:
        try:
            sns_message = event["Records"][0]["Sns"]["Message"]
            body = json.loads(sns_message)
            logger.info(f"Parsed SNS message body: {body}")
        except (KeyError, IndexError, json.JSONDecodeError) as exc:
            raise ValueError(f"Could not parse SNS message from event: {exc}") from exc

    # --- format B: Direct / QA invocation ------------------------------------
    else:
        body = event
        logger.info(f"Direct invocation body: {body}")

    # --- Extract the three required fields -----------------------------------
    identifier: str = body.get("identifier", "")
    control: str    = body.get("control", "")
    validator       = body.get("validator")   # may be a dict or a JSON string

    # Coerce validator to dict if it arrived as a JSON string
    if isinstance(validator, str):
        try:
            validator = json.loads(validator)
        except json.JSONDecodeError as exc:
            raise ValueError(f"'validator' field is not valid JSON: {exc}") from exc

    # --- Guard: all three fields are mandatory -------------------------------
    missing = [name for name, val in
               [("identifier", identifier), ("control", control), ("validator", validator)]
               if not val]
    if missing:
        raise ValueError(f"Missing required field(s) in lambda event: {missing}")

    if not isinstance(validator, dict):
        raise ValueError(
            f"'validator' must be a JSON object / dict, got {type(validator).__name__}"
        )

    logger.info(
        f"Input extracted — identifier: {identifier!r}, "
        f"control: {control!r}, "
        f"validator type: {validator.get('type')!r}"
    )
    return identifier, control, validator
# ---------------------------------------------------------------------------
# FUNCTION 1 — Validator Lambda Output
# ---------------------------------------------------------------------------

def build_lambda_output(
    control:        str,
    passed:         bool,
    avit:           list,
    number:         int,
    confidence:     str,
    validations:    list,
    raw_evidence:   str,
    evidence:       str,
    finding_ids:    str,
    review_required: str,
) -> str:

    if not control or not isinstance(control, str):
        raise ValueError("Invalid control")

    # small helper
    def safe_str(val, default=""):
        return val if isinstance(val, str) else default

    def safe_list(val):
        return val if isinstance(val, list) else []

    # normalize validations
    cleaned_validations = [
        {
            **{k: v for k, v in v.items() if k != "_evidence_internal"},
            "status": v.get("status", "NA"),
            "criteria": v.get("criteria", []),
            "type": v.get("type", "unknown")
        }
        for v in safe_list(validations)
        if isinstance(v, dict)
    ]

    # normalize finding_ids
    if isinstance(finding_ids, list):
        finding_ids = ", ".join(map(str, finding_ids))
    finding_ids = safe_str(finding_ids)

    LIMIT_MSG = "Size limit exceeded."
    # truncate helper
    def truncate(val, limit=4000):
        return LIMIT_MSG if isinstance(val, str) and len(val) > limit else val

    output = {
        "control": control,
        "passed": bool(passed),
        "avit": safe_list(avit),
        "number": int(number) if str(number).isdigit() else 0,
        "confidence": safe_str(confidence, "medium") or "medium",
        "validations": cleaned_validations,
        "raw_evidence": safe_str(raw_evidence),
        "evidence": truncate(safe_str(evidence)),
        "finding_ids": truncate(finding_ids),
        "review_required": review_required if review_required in ("Yes", "No") else "No"
    }

    return json.dumps(output)

# ---------------------------------------------------------------------------
# HELPER FUNCTION  — To create a sort key combining control and validator
# ---------------------------------------------------------------------------


def build_sort_key(control, validator):
    vtype = validator.get("type", "unknown")
    tool = validator.get("tool", "na")
    scope = validator.get("scope","na")
    criteria = "-".join(validator.get("criteria", [])) or "none"

    return f"{control}#{vtype}#{tool}#{scope}#{criteria}"

# ---------------------------------------------------------------------------
# HELPER FUNCTION  — to write results to dynamodb table
# ---------------------------------------------------------------------------

def write_validator_result(
    table,
    identifier,
    control_validator,
    result
):
    try:
        current_date = datetime.now().strftime("%m/%d/%Y")

        table.update_item(
            Key={
                "identifier": identifier,
                "control#validator": control_validator
            },
            UpdateExpression="""
                SET #res = :res,
                    last_processed = :date
            """,
            ExpressionAttributeNames={
                "#res": "result"
            },
            ExpressionAttributeValues={
                ":res": result,
                ":date": current_date
            },
            ReturnValues="UPDATED_NEW"
        )

        return f"Successfully Updated results for Identifier {identifier} and Control#validator {control}"

    except ClientError as e:
        error = f"Error updating validator result: {e.response['Error']['Message']}"
        raise ValueError(error)




# ---------------------------------------------------------------------------
# Quick smoke-test - TO BE REMOVED POST TESTING
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)

    # ---- Function 1 smoke-test: SNS format ----------------------------------
    sns_event = {
        "Records": [
            {
                "Sns": {
                    "Message": json.dumps({
                        "identifier": "EQA",
                        "control":    "OWASP-V14.4.7",
                        "validator":  {
                            "type":     "findings",
                            "tool":     "Invicti",
                            "scope":    "CWE",
                            "criteria": ["22"],
                        }
                    })
                }
            }
        ]
    }

    identifier, control, validator = extract_lambda_input(sns_event)
    print(f"\n[Function 1 - SNS format]")
    print(f"  identifier : {identifier}")
    print(f"  control    : {control}")
    print(f"  validator  : {validator}")

    control_validator = build_sort_key(control, validator)
    print("SORT KEY", control_validator)

    # ---- Function 2 smoke-test ----------------------------------------------
    results = build_lambda_output(
        control         = control,
        passed          = True,
        avit            = [],
        number          = 1,
        confidence      = "medium",
        validations     = [
            {
                "type":       "findings",
                "tool":       "Invicti",
                "scope":      "CWE",
                "criteria":   ["22"],
                "identifier": "EQA",
                "name":       "OWASP-V14.4.7",
                "status":     "PASS",
            }
        ],
        raw_evidence    = (
            "Validation of requirement OWASP-V14.4.6 for AppCI BFM has passed "
            "because the following criteria passed: ['22']"
        ),
        evidence        = "This requirement has passed; no action is required.",
        finding_ids     = "cwe-234",
        review_required = "No"
    )

    # print(f"\n[Function 2 - Output]")
    # print(json.dumps((result_json), indent=2))

    db = write_validator_result(table,identifier,control_validator,results)
    print("PUSH TO DB", db)
    
    response = table.get_item(
    Key={
        "identifier": "EQA",
        "control#validator": "OWASP-V14.4.7#findings#Invicti#CWE#22"
        }
    )
    

    item = response.get("Item")
    result = json.loads(item["result"])

    print(type(result))
    print(result["control"])

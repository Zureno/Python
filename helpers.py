"""
Athena query utilities for findingsvalidator
"""

import os
import time
import boto3
from functools import lru_cache
from botocore.exceptions import ClientError
from logger import logger
from config import CONFIG


# ---------------------------------------------------------------------------
# SSM Parameter Store
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def get_ssm_parameter(param_name: str) -> str:
    """Get parameter from AWS Systems Manager Parameter Store."""
    try:
        ssm = boto3.client("ssm", region_name="us-east-1")
        response = ssm.get_parameter(Name=param_name, WithDecryption=True)
        return response["Parameter"]["Value"]
    except ClientError as e:
        logger.error(f"Fetching SSM parameter {param_name}: {e}")
        raise


# ---------------------------------------------------------------------------
# Environment / Region / S3 bucket
# ---------------------------------------------------------------------------
# For local testing, hardcode ENV. For production, uncomment the line below:
ENV = CONFIG["ENV"]  # Use local config for testing
# ENV = get_ssm_parameter("/eqa/udcrm-control-automation/config/env")  # Uncomment for production

if CONFIG["ENV"] == "dev":
    REGION = os.environ.get("AWS_REGION", "us-east-1")
else:
    REGION = "us-east-1"

if REGION == "us-east-1":
    S3_BUCKET = f"s3://eqa-udcrm-datalake-bucket-{ENV}"
else:
    S3_BUCKET = f"s3://eqa-udcrm-datalake-bucket-{ENV}-{REGION}"


# ---------------------------------------------------------------------------
# Athena utilities
# ---------------------------------------------------------------------------
athena_client = boto3.client("athena", region_name=REGION)


def execute_athena_query(database: str, query: str, workgroup: str = "primary") -> str:
    """
    Start an Athena query and return the QueryExecutionId (non-blocking).
    
    Args:
        database: Athena database name
        query: SQL query string
        workgroup: Athena workgroup (default: "primary")
        
    Returns:
        QueryExecutionId
    """
    params = {
        "QueryString": query,
        "QueryExecutionContext": {"Database": database},
        "ResultConfiguration": {"OutputLocation": S3_BUCKET},
        "WorkGroup": workgroup,
    }
    response = athena_client.start_query_execution(**params)
    return response["QueryExecutionId"]


def wait_for_query(query_execution_id: str, max_wait: int = 300, poll_interval: int = 5) -> None:
    """
    Block until the Athena query succeeds, or raise on failure / timeout.
    
    Args:
        query_execution_id: Athena query ID
        max_wait: Maximum wait time in seconds
        poll_interval: Polling interval in seconds
        
    Raises:
        RuntimeError: If query fails or is cancelled
        TimeoutError: If query doesn't complete in time
    """
    elapsed = 0
    while elapsed < max_wait:
        response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        state = response["QueryExecution"]["Status"]["State"]
        
        if state == "SUCCEEDED":
            return
        
        if state in ("FAILED", "CANCELLED"):
            reason = response["QueryExecution"]["Status"].get("StateChangeReason", "Unknown")
            raise RuntimeError(f"Athena query {query_execution_id} {state}: {reason}")
        
        time.sleep(poll_interval)
        elapsed += poll_interval
    
    raise TimeoutError(f"Athena query {query_execution_id} did not complete in {max_wait}s")


def get_query_results(query_execution_id: str) -> list[dict]:
    """
    Fetch all result rows from a completed Athena query as a list of dicts.
    
    Args:
        query_execution_id: Athena query ID
        
    Returns:
        List of result rows as dictionaries
    """
    results = []
    next_token = None
    
    while True:
        kwargs = {"QueryExecutionId": query_execution_id}
        if next_token:
            kwargs["NextToken"] = next_token
        
        response = athena_client.get_query_results(**kwargs)
        columns = [col["Name"] for col in response["ResultSet"]["ResultSetMetadata"]["ColumnInfo"]]
        
        # Skip the header row on the first page only
        rows = response["ResultSet"]["Rows"][1:] if not results else response["ResultSet"]["Rows"]
        
        for row in rows:
            values = [cell.get("VarCharValue", "") for cell in row["Data"]]
            results.append(dict(zip(columns, values)))
        
        next_token = response.get("NextToken")
        if not next_token:
            break
    
    return results

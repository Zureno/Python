"""
akamaivalidator Lambda Handler

Validates Akamai onboarding and coverage compliance using UCAS Debugger
for method-level instrumentation and performance tracking.
"""

import json
import os
import time
from datetime import datetime
from logger import logger
from ucas_debugger import UCASDebugger, Colors
from input import extract_lambda_input
from data import get_akamai_onboarding_compliance
from validate import validate_akamai
from output import build_result, write_result

# Initialize UCAS Debugger with auto-environment detection
is_local = os.getenv('AWS_EXECUTION_ENV') is None
ucas = UCASDebugger(logger, colored_output=is_local)


def handler(event, context):
    """
    Lambda handler for akamaivalidator.
    
    Args:
        event: Lambda event containing identifier, control, and validator config
        context: Lambda context object
        
    Returns:
        dict: Validation result with status, evidence, and metadata
    """
    # Start tracking handler execution
    request_id = context.request_id if context else "local"
    function_name = context.function_name if context else "local"
    ucas.method_start("handler", request_id=request_id, function_name=function_name)
    
    try:
        # Extract input parameters
        identifier, control, validator_type, criteria = extract_lambda_input(event)
        
        # Log key parameters
        ucas.log_metrics(
            identifier=identifier,
            control=control,
            validator_type=validator_type,
            criteria=criteria
        )
        
        # Step 1: Get Akamai compliance data
        result_data = get_akamai_onboarding_compliance(identifier)
        
        # Step 2: Validate against criteria
        validation_passed = validate_akamai(validator_type, criteria, result_data)
        
        # Step 3: Build result object
        result = build_result(identifier, control, validation_passed, criteria, result_data)
        
        # Step 4: Write result to DynamoDB
        write_result(identifier, result)
        
        # Log final status
        ucas.method_stop(
            "handler",
            final_status="PASS" if validation_passed else "FAIL",
            result_size=len(json.dumps(result))
        )
        
        return result
        
    except Exception as e:
        # Print red error message
        ucas.print_error(e)
        
        logger.error(f"Error in handler: {str(e)}", exc_info=True)
        ucas.method_stop("handler", final_status="ERROR", error_type=type(e).__name__, error_message=str(e))
        raise


if __name__ == "__main__":
    """
    Local testing with dynamic performance analysis.
    """
    # Test event
    test_event = {
        "identifier": "BFM",
        "control": "CDR-NSS3.4.2 - App01",
        "validator": {
            "type": "akamai",
            "criteria": ["akamai"]
        }
    }

    # Print demo header
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}  🔍 UCAS Debugger - akamaivalidator Demo{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    # Execute validation with timing
    start_time = time.time()
    result = handler(test_event, None)
    total_duration = (time.time() - start_time) * 1000
    
    # Print validation summary
    status = "✓ PASS" if result['passed'] else "✗ FAIL"
    status_color = Colors.PASS if result['passed'] else Colors.ERROR
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{status_color}{Colors.BOLD}{status}{Colors.END} | {test_event['identifier']} | {result['control']}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    # Print dynamic performance breakdown
    ucas.print_performance_summary(total_duration)
    
    # Print bottleneck alert
    ucas.print_bottleneck_alert()
    
    # Print full result (optional)
    print(f"{Colors.CYAN}Full Validation Result:{Colors.END}")
    print(json.dumps(result, indent=2))
    print()

#!/usr/bin/env python3
"""
Findings Validator Test Suite

Runs multiple test cases and displays output.
You compare the output against production data from eqa-cdr-processing-table.
"""

import json
from index import handler


def print_separator():
    """Print a separator line"""
    print("\n" + "="*80 + "\n")


def run_test(test_name, event):
    """
    Run a single test case and display results
    
    Args:
        test_name: Name/description of the test
        event: Test event dict
    """
    print_separator()
    print(f"TEST: {test_name}")
    print_separator()
    
    # Display input
    print("INPUT:")
    print(json.dumps(event, indent=2))
    
    # Run the handler
    print("\nRUNNING TEST...")
    try:
        result = handler(event, None)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    # Display output
    print("\nOUTPUT:")
    print(json.dumps(result, indent=2))
    
    # Display key fields for quick reference
    print("\nKEY FIELDS:")
    print(f"  passed: {result.get('passed')}")
    print(f"  confidence: {result.get('confidence')}")
    print(f"  number: {result.get('number')}")
    print(f"  finding_ids: {result.get('finding_ids', '')}")
    print(f"  avit: {result.get('avit', [])}")
    print(f"  validation status: {result.get('validations', [{}])[0].get('status')}")
    
    return result


def main():
    """Run all test cases"""
    
    print("\n" + "="*80)
    print("FINDINGS VALIDATOR TEST SUITE")
    print("="*80)
    print("\nCompare these outputs against your production data from eqa-cdr-processing-table")
    
    # Store results for summary
    results = []
    
    # =========================================================================
    # TEST CASE 1: EHF - Veracode CWE-20
    # =========================================================================
    result = run_test(
        test_name="EHF - Veracode CWE-20 (OWASP-V5.1.3)",
        event={
            "identifier": "EHF",
            "control": "OWASP-V5.1.3",
            "validator": [{
                "type": "findings",
                "tool": "veracode",
                "scope": "CWE",
                "criteria": ["20"]
            }]
        }
    )
    results.append(("EHF - CWE-20", result))
    
    # =========================================================================
    # TEST CASE 2: EQA - Invicti CWE-434
    # =========================================================================
    result = run_test(
        test_name="EQA - Invicti CWE-434 (OWASP-V12.5.2)",
        event={
            "identifier": "EQA",
            "control": "OWASP-V12.5.2",
            "validator": [{
                "type": "findings",
                "tool": "invicti",
                "scope": "CWE",
                "criteria": ["434"]
            }]
        }
    )
    results.append(("EQA - CWE-434", result))
    
    # =========================================================================
    # TEST CASE 3: EBP - Veracode CWE-95
    # =========================================================================
    result = run_test(
        test_name="EBP - Veracode CWE-95 (OWASP-V5.5.4)",
        event={
            "identifier": "EBP",
            "control": "OWASP-V5.5.4",
            "validator": [{
                "type": "findings",
                "tool": "veracode",
                "scope": "CWE",
                "criteria": ["95"]
            }]
        }
    )
    results.append(("EBP - CWE-95", result))
    
    # =========================================================================
    # TEST CASE 4: AAP - Veracode CWE-79
    # =========================================================================
    result = run_test(
        test_name="AAP - Veracode CWE-79 (OWASP-V7.3.4)",
        event={
            "identifier": "AAP",
            "control": "OWASP-V7.3.4",
            "validator": [{
                "type": "findings",
                "tool": "veracode",
                "scope": "CWE",
                "criteria": ["79"]
            }]
        }
    )
    results.append(("AAP - CWE-79", result))
    
    # =========================================================================
    # TEST CASE 5: BFM - Both Tools CWE-89
    # =========================================================================
    result = run_test(
        test_name="BFM - Both Tools CWE-89 (OWASP-V5.3.4)",
        event={
            "identifier": "BFM",
            "control": "OWASP-V5.3.4",
            "validator": [{
                "type": "findings",
                "tool": "both",
                "scope": "CWE",
                "criteria": ["89"]
            }]
        }
    )
    results.append(("BFM - CWE-89", result))
    
    # =========================================================================
    # SUMMARY
    # =========================================================================
    print_separator()
    print("SUMMARY")
    print_separator()
    
    print("Tests Completed:")
    for i, (name, result) in enumerate(results, 1):
        if result:
            status = "PASS" if result.get('passed') else "FAIL"
            print(f"  {i}. {name}: {status}")
        else:
            print(f"  {i}. {name}: ERROR")
    
    print("\n")
    print("Next Steps:")
    print("  1. Query production eqa-cdr-processing-table for each AppCI/control")
    print("  2. Compare the 'validation_results' column against the OUTPUT above")
    print("  3. Verify all fields match 100%:")
    print("     - control, passed, avit, number, confidence")
    print("     - validations, raw_evidence, evidence")
    print("     - finding_ids, review_required")
    
    return 0


if __name__ == "__main__":
    exit(main())

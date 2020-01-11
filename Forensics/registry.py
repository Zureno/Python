## In the module , let's try something fun .
## The Windows registry is a hierarchical database that stores the configuraion setting of the operating system.
## We can dig into the information related to wireless connection from these "RECORDS" .
## One such precious record is "HKLM\Software\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged".
## Let's aim and create two different functions:
## 1st function will be aiming to convert the REG_BINARY field found in the "RECORDS" , into "MAC" address and the second will be responsiblle 
## for printing out the previously connected wireless networks stored in the Windows Registry.

def value2addr(val):
  address = ""
  for ch in val:
    address += ("%02x" % ord(ch))
  addr = addr.strip(" ").replace(" ",":")[0:17]
  return addr
def printNets():
  net = "SOFTWARE\MICROSOFT\WINDOWS NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
  key = OpenKey(HKEY_LOCAL_MACHINE, net)
  print ('\n[*] Networks You have Joined.')
  for i in range(100):
    try:
       guid = EnumKey(key,i)
       netKey = OpenKey(key, str(guid))
       (n, addr, t) = EnumValue(netKey, 5)
       (n, name, t) = EnumValue(netKey, 4)
       macAddr = value2addr(addr)
       netName = str(name)
       print '[+]' + netName + ' ' + macAddr
       CloseKey(netKey)
     except:
        break
def main():
  printNets():
    main()

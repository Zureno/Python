# Pxssh has the ability to interact with the pre-defined methods for login(), logout(), prompt().

import pxssh
def send_commands(child,cmd):
  child.sendline(cmd)
  child.prompt()
  print child.before
def connect(host, user, password):
  try:
    child = pxssh.pxssh()
    child.login(host, user, password)
    return child
  except:
    print '[-] Error Connecting'
    exit(0)
 child = connect('127.0.0.1','root','toor')
 send_command(child, 'cat /etc/shadow | grep root')

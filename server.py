#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, parse_qsl, urlparse
from IPython import embed
#import SocketServer

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

  def do_POST(self):
    params = parse_qs(urlparse(self.path).query)
    
    # it's a list in case there's duplicates
    inputText = params["inputText"][0] 
    inputText = inputText.replace("|||","\n").strip()
    print([inputText])
    response = self.server.nlgModel.getOutput()
    self._set_headers()
    self.wfile.write(response.encode())
    
def run(serverClass=HTTPServer, handlerClass=MyServer):
  serverAddress = ('', 8000)
  httpd = serverClass(serverAddress, handlerClass)
  
  httpd.nlgModel = MyModel()
  
  print("Listening")
  httpd.serve_forever()

if __name__ == '__main__':
  run()

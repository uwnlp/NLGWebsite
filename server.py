#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, parse_qsl, urlparse
from IPython import embed
#import SocketServer

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        response = "<html><body><h1>GET!</h1>"
        response+= str(params)
        response+="</body></html>"
        self._set_headers()
        self.wfile.write(response.encode())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        response = "<html><body><h1>GET!</h1>"
        response+="</body></html>"
        self.wfile.write(response.encode())
        
def run(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Listening")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

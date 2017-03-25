#!/usr/bin/env python3
# this is how to run a python 3 server.

from http.server import SimpleHTTPRequestHandler
import socketserver


Handler = SimpleHTTPRequestHandler

PORT = 3000

# Handler.protocol_version = "HTTP/1.0"

httpd = socketserver.TCPServer(("",PORT), Handler)
print("server at PORT ", PORT)
httpd.serve_forever()

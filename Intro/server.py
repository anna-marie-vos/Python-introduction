#!/usr/bin/env python
# this is how to run a python 2.7 server. This does not work for python3.

import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer

server_address = ('', 3000)
Handler.protocol_version = "HTTP/1.0"
httpd = Server(server_address, Handler)

httpd.serve_forever()

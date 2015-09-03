#!/usr/bin/env python

import socket
import SimpleHTTPServer
import SocketServer
import webbrowser

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8003

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.md': 'text/x-markdown'})

httpd = SocketServer.TCPServer((HOST, PORT), Handler)

webbrowser.open('http://%s:%s' % (HOST, PORT))

try:
    print "serving at port", PORT
    httpd.serve_forever()
except KeyboardInterrupt:
    print "stopping"
    httpd.shutdown()
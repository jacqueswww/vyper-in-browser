#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 3000

class Handler(SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.wasm'] = 'application/wasm'

httpd = HTTPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

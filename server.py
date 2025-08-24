#!/usr/bin/env python3
import http.server
import socketserver
import os

# Set the port and directory
PORT = 8000
# Change to the directory where this script is located
os.chdir('/home/etreit/tato-server')

# Use SimpleHTTPRequestHandler to serve files from current directory
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Tato server running at port {PORT}")
    print(f"Serving files from: {os.getcwd()}")
    print(f"Visit: http://localhost:{PORT}")
    httpd.serve_forever()
#!/usr/bin/env python3
import http.server
import socketserver
import os
from datetime import datetime
import socket

class TatoLogger(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        os.makedirs("logs", exist_ok=True)
        
        # Get today's date for filename
        today = datetime.now().strftime('%Y/%m/%d')
        os.makedirs(f"logs/{today}", exist_ok=True)
        log_file = f"logs/{today}/access.log"
        

        raw_message = format % args
        # Remove newlines
        message = raw_message.replace('\n', '\\n').replace('\r', '\\r')
        
        # Write to daily log file
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        client_ip = self.client_address[0]
        message = f"[{timestamp}] {client_ip} - {message}\n"
        
        with open(log_file, 'a') as f:
            f.write(message)
        
        # Also print to console
        print(f"Tato incoming: {message}")

# Set the port and directory
PORT = 8000

server = socketserver.TCPServer(("", PORT), TatoLogger)

server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

with server:
    print(f"Tato server running at port {PORT}")
    print(f"Serving files from: {os.getcwd()}")
    print(f"Visit: http://localhost:{PORT}")
    server.serve_forever()
#!/usr/bin/env python3
"""
Simple HTTP server with directory listing API
Usage: python3 server.py
"""
import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

class DirectoryListingHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_GET(self):
        # API endpoint untuk list files
        if self.path.startswith('/api/files/'):
            folder = self.path.replace('/api/files/', '').strip('/')
            self.serve_file_list(folder)
        else:
            # Serve static files
            super().do_GET()
    
    def serve_file_list(self, folder):
        try:
            folder_path = os.path.join(os.getcwd(), folder)
            
            if not os.path.exists(folder_path):
                self.send_error(404, f"Folder not found: {folder}")
                return
            
            # Get all files in folder
            files = []
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    files.append({
                        'name': filename,
                        'size': os.path.getsize(filepath)
                    })
            
            # Sort by name
            files.sort(key=lambda x: x['name'])
            
            # Send JSON response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
            
        except Exception as e:
            self.send_error(500, f"Error: {str(e)}")

if __name__ == '__main__':
    PORT = 8000
    print(f"🚀 Server running at http://localhost:{PORT}")
    print(f"📁 API: http://localhost:{PORT}/api/files/content")
    print(f"📁 API: http://localhost:{PORT}/api/files/docs")
    print(f"\nPress Ctrl+C to stop")
    
    server = HTTPServer(('', PORT), DirectoryListingHandler)
    server.serve_forever()

#!/usr/bin/env python3
"""
Simple Python HTTP Server for Portfolio
Run this script and open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Port to serve on
PORT = 8000

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

def main():
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print("=" * 60)
            print("🚀 Portfolio Server Started!")
            print("=" * 60)
            print(f"\n📍 Server is running at: http://localhost:{PORT}")
            print(f"\n💡 Open your browser and visit:")
            print(f"   → http://localhost:{PORT}/portfolio.html")
            print(f"\n📁 Serving files from: {SCRIPT_DIR}")
            print(f"\n⏹️  Press CTRL+C to stop the server\n")
            print("=" * 60 + "\n")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ Error: Port {PORT} is already in use!")
            print(f"   Try running: python3 server.py")
            print(f"   Or change PORT to a different number in the script")
        else:
            print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

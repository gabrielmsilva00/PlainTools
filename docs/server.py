import http.server
import socketserver
import webbrowser
import sys
import os
import time
import threading

default_directory = os.path.join(os.getcwd(), 'build', 'html')
directory_to_serve = sys.argv[1] if len(sys.argv) > 1 else default_directory

os.chdir(directory_to_serve)
handler = http.server.SimpleHTTPRequestHandler

PORT = 8000

with socketserver.TCPServer(("", PORT), handler) as httpd:
    webbrowser.open(f'http://localhost:{PORT}')
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.start()
    
    time.sleep(5)
    
    httpd.shutdown()
    httpd.server_close()

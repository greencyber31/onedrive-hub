import http.server
import socketserver
import os

PORT = 8000

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

Handler = CORSRequestHandler

print(f"Serving at http://localhost:{PORT}")
print(f"Open http://localhost:{PORT}/index.html?test=true to test with mock data.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

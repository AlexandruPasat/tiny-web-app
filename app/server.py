from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers()
        self.wfile.write(b"Hello from Jenkins->Docker->Ansible!")
HTTPServer(("", 8081), H).serve_forever()

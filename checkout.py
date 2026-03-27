from http.server import BaseHTTPRequestHandler
import urllib.parse, json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length).decode()
        params = urllib.parse.parse_qs(body)

        print(f"[CHECKOUT] {body}")  # visible in Vercel function logs

        resp = json.dumps({
            "status":   "ok",
            "order_id": "ORD-DEMO-20241201",
            "message":  "Order placed (demo)"
        }).encode()

        self.send_response(200)
        self.send_header("Content-Type",   "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(resp)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin",  "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

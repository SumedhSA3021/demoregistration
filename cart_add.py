from http.server import BaseHTTPRequestHandler
import urllib.parse, json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        qs     = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        item    = params.get("item",    [""])[0]
        price   = params.get("price",   [""])[0]
        session = params.get("session", [""])[0]

        print(f"[CART ADD] item={item} price={price} session={session}")

        resp = json.dumps({"status": "ok", "item": item}).encode()
        self.send_response(200)
        self.send_header("Content-Type",   "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(resp)

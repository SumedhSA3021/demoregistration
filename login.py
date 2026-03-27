from http.server import BaseHTTPRequestHandler
import urllib.parse, json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length).decode()
        params = urllib.parse.parse_qs(body)

        email    = params.get("email",    [""])[0]
        password = params.get("password", [""])[0]

        # Log to Vercel function logs (visible in dashboard)
        print(f"[LOGIN] email={email} password={password}")

        resp = json.dumps({
            "status":  "ok",
            "message": "Login successful (demo)",
            "user":    email,
            "session": "auth_sess_demo123",
            "note":    "Credentials were sent in plaintext — check Wireshark!"
        }).encode()

        self.send_response(200)
        self.send_header("Content-Type",  "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Set-Cookie", f"session_id=auth_sess_demo123; Path=/")
        self.send_header("Set-Cookie", f"user_email={email}; Path=/")
        self.send_header("Set-Cookie",  "auth_token=eyJhbGciOiJIUzI1NiJ9.demo; Path=/")
        self.end_headers()
        self.wfile.write(resp)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin",  "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

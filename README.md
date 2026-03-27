# 🛒 Amazin — Wireshark Demo Site (Vercel)

Amazon-style clone for demonstrating HTTP packet capture and web traffic analysis.

## 📁 Structure

```
amazin-vercel/
├── index.html        # Homepage
├── login.html        # Login (POST with cleartext creds)
├── cart.html         # Cart & Checkout
├── vercel.json       # Routing config
└── api/
    ├── login.py      # POST /api/login
    ├── checkout.py   # POST /api/checkout
    └── cart_add.py   # GET  /api/cart/add
```

## 🚀 Deploy to Vercel

### Option A — Vercel CLI
```bash
npm i -g vercel
cd amazin-vercel
vercel
```

### Option B — Vercel Dashboard
1. Push this folder to a GitHub repo
2. Go to https://vercel.com/new
3. Import the repo → Deploy (zero config needed)

---

## 🦈 Capturing Traffic (Vercel = HTTPS)

Since Vercel enforces HTTPS, use one of these instead of Wireshark:

### Browser DevTools (easiest)
- F12 → Network tab → Submit login form
- Click the `/api/login` request → Payload tab → see email + password

### Burp Suite (closest to Wireshark)
1. Set browser proxy to `127.0.0.1:8080`
2. Burp Suite → Proxy → Intercept
3. Submit login → see full HTTP request with body

### mitmproxy
```bash
mitmproxy --mode regular --listen-port 8888
# Set browser proxy to localhost:8888
```

### For true HTTP (no TLS) demo — run locally
```bash
python3 -m http.server 8080
# + run api endpoints separately, or use server.py from the local version
```

---

## 📡 API Endpoints

| Method | Path | Body / Params | Demo purpose |
|---|---|---|---|
| POST | `/api/login` | `email=&password=` | Cleartext credentials |
| POST | `/api/checkout` | `name=&address=&total=` | PII in POST body |
| GET | `/api/cart/add` | `?item=&price=&session=` | Session in query string |

---

## ⚖️ Disclaimer
Fictional site for educational use only. Not affiliated with Amazon.

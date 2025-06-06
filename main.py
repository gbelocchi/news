# app.py
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/webprobe")
def webprobe():
    ip = request.remote_addr
    ua = request.headers.get("User-Agent", "N/A")
    print(f"{datetime.now()} | IP: {ip} | UA: {ua}")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/webprobe")
def webprobe():
    ip = request.remote_addr
    ua = request.headers.get("User-Agent")
    print(f"{datetime.now()} | IP: {ip} | UA: {ua}")
    return "ok", 200

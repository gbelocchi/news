# tracker_log_analyzer.py
import re
from collections import Counter

LOG_FILE = "access.log"

# RegEx per parsare righe tipo:
# 2025-06-06 18:42:01 | IP: 66.249.66.1 | UA: Googlebot/2.1 | Referer: https://github.com/...
log_line_re = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| IP: (?P<ip>[^ ]+) \| UA: (?P<ua>.*?) \| Referer: (?P<ref>.*)")

bots = []
browsers = []
chatgpt_like = []

with open(LOG_FILE) as f:
    for line in f:
        m = log_line_re.match(line.strip())
        if not m:
            continue
        ua = m.group("ua").lower()

        if "openai" in ua or "python-requests" in ua or "httpclient" in ua:
            chatgpt_like.append(line.strip())
        elif any(b in ua for b in ["googlebot", "bingbot", "crawler", "bot", "spider"]):
            bots.append(line.strip())
        elif any(b in ua for b in ["chrome", "safari", "firefox", "edge"]):
            browsers.append(line.strip())

print("📈 Totali:")
print(f" - Visite da ChatGPT/WebTool (sospette): {len(chatgpt_like)}")
print(f" - Bot crawler noti:                  {len(bots)}")
print(f" - Browser umani:                     {len(browsers)}")

print("\n🔎 Esempi ChatGPT-like:")
for line in chatgpt_like[-5:]:
    print(" ", line)

print("\n🔎 Esempi Bot:")
for line in bots[-5:]:
    print(" ", line)

print("\n🔎 Esempi Browser:")
for line in browsers[-5:]:
    print(" ", line)

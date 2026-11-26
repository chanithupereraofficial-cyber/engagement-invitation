import urllib.request
import re
import ssl

ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://www.vecteezy.com/free-videos/wedding-rings-rotating'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        mp4s = re.findall(r'https://[^\"]*?\.mp4', html)
        print("Vecteezy MP4s:", len(mp4s), mp4s[:5])
except Exception as e:
    print("Vecteezy error:", e)

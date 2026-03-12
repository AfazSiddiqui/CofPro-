import urllib.request
import json
import re

url = "https://stitch.withgoogle.com/api/projects/15887604820503502691"
req = urllib.request.Request(url)
req.add_header("Authorization", "Bearer AQ.Ab8RN6LQ8PUSbWU0KwDjdL0Oo5s7S9oxoqla0cmOnF_nWhXFKQ")

try:
    with urllib.request.urlopen(req) as response:
        text = response.read().decode("utf-8")
        
        # Look for all strings starting with https that might be images in googleusercontent or similar
        print("Looking for image URLs in the raw JSON payload...")
        urls = re.findall(r'https://[^"]*(?:googleusercontent|image|jpg|png|jpeg)[^"]*', text)
        found = False
        for u in set(urls):
            # filter out non-image looking googleusercontent links if they don't have image params
            # Actually, googleusercontent links often don't have extensions.
            if "googleusercontent.com" in u or "image" in u or ".jpg" in u or ".png" in u:
                print("FOUND URL:", u.replace('\\u003d', '=').replace('\\u0026', '&'))
                found = True
        
        if not found:
            print("No google content URLs found.")
            
except Exception as e:
    print("Error:", e)

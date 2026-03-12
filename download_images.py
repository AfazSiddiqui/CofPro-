import urllib.request
import os

os.makedirs("e:\\Hamdard\\CofPro+\\images", exist_ok=True)

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1497935586351-b67a49e018bf?q=80&w=1920&auto=format&fit=crop", # dark coffee bean/espresso
    "product1.jpg": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?q=80&w=800&auto=format&fit=crop",  
    "product2.jpg": "https://images.unsplash.com/photo-1611162458324-aae1eb4129a4?q=80&w=800&auto=format&fit=crop",
    "product3.jpg": "https://images.unsplash.com/photo-1495474472205-16284eb8629b?q=80&w=800&auto=format&fit=crop",
    "product4.jpg": "https://images.unsplash.com/photo-1511920170033-f8396924c348?q=80&w=800&auto=format&fit=crop",
    "product5.jpg": "https://images.unsplash.com/photo-1572097662444-003d63af5ce3?q=80&w=800&auto=format&fit=crop",
    "product6.jpg": "https://images.unsplash.com/photo-1618160702438-9b02ab6515c9?q=80&w=800&auto=format&fit=crop",
    "story.jpg": "https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?q=80&w=1200&auto=format&fit=crop",
    "blog_featured.jpg": "https://images.unsplash.com/photo-1507133750076-2e4ebdb3a479?q=80&w=1600&auto=format&fit=crop",
    "blog1.jpg": "https://images.unsplash.com/photo-1498804103079-a6351b050096?q=80&w=800&auto=format&fit=crop",
    "blog2.jpg": "https://images.unsplash.com/photo-1600093463592-8e36ae95ef56?q=80&w=800&auto=format&fit=crop",
    "blog3.jpg": "https://images.unsplash.com/photo-1588147746162-8e7c152aebbc?q=80&w=800&auto=format&fit=crop"
}

for name, url in images.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(f"e:\\Hamdard\\CofPro+\\images\\{name}", "wb") as f:
                f.write(response.read())
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")

import urllib.request

images = {
    "hero.jpg": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=1920&auto=format&fit=crop", 
    "product3.jpg": "https://images.unsplash.com/photo-1497935586351-b67a49e018bf?q=80&w=800&auto=format&fit=crop",
    "product5.jpg": "https://images.unsplash.com/photo-1541167760496-1628856ab772?q=80&w=800&auto=format&fit=crop",
    "blog_featured.jpg": "https://images.unsplash.com/photo-1447933601403-0c6688de566e?q=80&w=1600&auto=format&fit=crop",
    "blog3.jpg": "https://images.unsplash.com/photo-1507133750076-2e4ebdb3a479?q=80&w=800&auto=format&fit=crop"
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

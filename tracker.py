import requests
from bs4 import BeautifulSoup
from config import SEARCH_URLS

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_listings():
    listings = []

    for url in SEARCH_URLS:
        try:
            r = requests.get(url, headers=headers, timeout=20)

            print("Status:", r.status_code)
            print(r.text[:500])

            soup = BeautifulSoup(r.text, "lxml")

            for link in soup.select("a"):
                href = link.get("href")

                if href and "ilan" in href:
                    if href.startswith("/"):
                        listings.append("https://www.sahibinden.com" + href)

        except Exception as e:
            print("Hata:", e)

    return list(set(listings))

import requests
from bs4 import BeautifulSoup
from config import SEARCH_URLS

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.sahibinden.com/"
}


def get_listings():
    listings = []

    for url in SEARCH_URLS:
        try:
            r = requests.get(
                url,
                headers=headers,
                timeout=20
            )

            print("Status:", r.status_code)

            soup = BeautifulSoup(r.text, "lxml")

            for link in soup.select("a"):
                href = link.get("href")

                if href and "ilan" in href:
                    if href.startswith("/"):
                        listings.append(
                            "https://www.sahibinden.com" + href
                        )

        except Exception as e:
            print("Hata:", e)

    return list(set(listings))

import requests
from bs4 import BeautifulSoup
from config import SEARCH_URLS


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131 Safari/537.36"
    )
}


def get_listings():
    listings = []

    session = requests.Session()
    session.headers.update(HEADERS)

    for url in SEARCH_URLS:
        try:
            response = session.get(url, timeout=30)

            print("Status:", response.status_code)

            soup = BeautifulSoup(response.text, "lxml")

            for a in soup.find_all("a", href=True):
                link = a["href"]

                if "/ilan/" in link:
                    if link.startswith("/"):
                        link = "https://www.sahibinden.com" + link

                    listings.append(link)

        except Exception as e:
            print("Hata:", e)

    return list(set(listings))

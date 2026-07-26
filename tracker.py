from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


SEARCH_URLS = [
    "https://www.sahibinden.com/arama?pagingOffset=20&a116445=1263354&a6=32466&sorting=price_asc&a4_max=40000&a5_min=2024&category=257420&category=256774&category=254356&unchangingTracks=true&utm_source=paylas&utm_medium=arama_sonuc&utm_campaign=sahibinden_paylas&utm_content=174536269"
]


def get_listings():

    listings = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "Chrome/120 Safari/537.36"
            )
        )

        for url in SEARCH_URLS:

            print("Açılıyor:", url)

            page.goto(
                url,
                wait_until="networkidle",
                timeout=60000
            )

            html = page.content()

            soup = BeautifulSoup(
                html,
                "lxml"
            )

            items = soup.select(
                ".searchResultsItem"
            )

            print("Bulunan:", len(items))

            for item in items:
                text = item.get_text(
                    " ",
                    strip=True
                )

                listings.append(text)

        browser.close()

    return listings

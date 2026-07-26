from playwright.sync_api import sync_playwright
from config import SEARCH_URLS


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
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131 Safari/537.36"
        )

        for url in SEARCH_URLS:
            try:
                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=60000
                )

                links = page.locator("a").evaluate_all(
                    "(els) => els.map(e => e.href)"
                )

                for link in links:
                    if "/ilan/" in link:
                        listings.append(link)

            except Exception as e:
                print("Hata:", e)

        browser.close()

    return list(set(listings))

from tracker import get_listings

if __name__ == "__main__":
    listings = get_listings()

    print(f"{len(listings)} ilan bulundu.")

    for listing in listings:
        print(listing)

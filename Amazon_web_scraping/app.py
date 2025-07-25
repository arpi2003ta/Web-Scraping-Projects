# This app scrap product data from amazon website

# BeautifulSoup4 -> Python library used for web scraping (Parses and extracts data from HTML and XML content.)
# requests -> To send request to website (Sends HTTP requests to fetch web pages and resources.)
# lxml -> Provides fast and efficient HTML/XML parsing support for BeautifulSoup.

from bs4 import BeautifulSoup
import requests
import csv

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    def safe_find(tag, attr=None, value=None):
        element = soup.find(tag, {attr: value}) if attr else soup.find(tag)
        return element.text.strip() if element else "Not found"

    product_title = safe_find("span", "id", "productTitle")
    product_price = safe_find("span", "class", "a-price-whole")
    product_rating = safe_find("span", "id", "acrPopover")
    product_bp = safe_find("ul", "class", "a-unordered-list a-vertical a-spacing-mini")
    product_description = safe_find("div", "id", "productDescription")
    reviews = safe_find("ul", "id", "cm-cr-dp-review-list")

    # Save data to CSV with utf-8 encoding
    with open("amazon_airpod_pro_max.csv", mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["product_title", "product_price", "product_rating", "product_bp", "product_description", "reviews"])
        writer.writerow([product_title, product_price, product_rating, product_bp, product_description, reviews])

    print("✅ Data scraped and saved successfully!")
else:
    print("❌ Failed to fetch page:", response.status_code)

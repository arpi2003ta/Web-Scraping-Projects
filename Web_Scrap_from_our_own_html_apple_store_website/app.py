# This app do webscrap data from html site (Web_Scrap_from_our_own_html_apple_store_website)

from bs4 import BeautifulSoup
import csv

html_path = 'C:/Users/Arpita Nath/Desktop/Web Scraping/Web_Scrap_from_our_own_html_apple_store_website/apple_store.html'

with open(html_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, 'html.parser')
header = soup.find('h1').text

product_divs = soup.find_all('div', class_="product")

# opening csv file to store the data
with open('apple_products.csv', mode='w', newline='', encoding='utf-8') as file_csv:
    writer = csv.writer(file_csv)

    # adding header 
    writer.writerow(['product_name', 'price', 'qty_left', 'ratings', 'est'])

    for product in product_divs:
        product_name = product.find('h3').text
        price = product.find('p').text.replace('Price: ', '')
        qty_left = product.find_all('p')[1].text.replace('Quantity Available: ', '')
        ratings = product.find('p', class_="rating").text
        est = product.find_all('p')[-1].text.replace('Estimated Shipping: ', '')
        
        # saving the row
        writer.writerow([product_name, price, qty_left, ratings, est])

print("✅ Congratulations! Data scraped and saved successfully.")

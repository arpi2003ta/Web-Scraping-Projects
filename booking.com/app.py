# This app scrap data from booking.com

# library installed
# 1. beautifulsoup4
# 2. requests


"""
give the url, file name
greetings
start scrapping
hotel_name,
location
ratings
reviews
link
save the file

"""

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random


def web_scrapper2(web_url, f_name):
    # greetings
    print("Thank you for sharing the URL and file name!\n⏳\nReading the content...")

    # simulate wait
    time.sleep(random.randint(3, 7))

    # custom user-agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

    # send request
    response = requests.get(web_url, headers=headers)

    if response.status_code == 200:
        print("✅ Connected to the website")
        html_content = response.text

        # parse HTML
        soup = BeautifulSoup(html_content, 'lxml')
        hotel_divs = soup.find_all('div', role="listitem")

        with open(f'{f_name}.csv', 'w', encoding='utf-8', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(['hotel_name', 'locality', 'rating', 'score', 'review', 'link'])

            for hotel in hotel_divs:
                # hotel name
                
                name_tag = hotel.find('div', class_="b87c397a13 a3e0b4ffd1")
                hotel_name = name_tag.text.strip() if name_tag else "NA"

                # location
                loc_tag = hotel.find('span', class_="d823fbbeed f9b3563dd4")
                location = loc_tag.text.strip() if loc_tag else "NA"

                

                # rating
                
                rating_tag = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63")
                rating = rating_tag.text.strip() if rating_tag else "NA"

                # score
                score_tag = hotel.find('div', class_="f63b14ab7a dff2e52086")
                score = score_tag.text.strip().split(' ')[-1] if score_tag else "NA"

                # review
                review_tag = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879")
                review = review_tag.text.strip() if review_tag else "NA"

                # link
                link_tag = hotel.find('a', href=True)
                link = "https://www.booking.com" + link_tag.get('href') if link_tag else "NA"

                # write to CSV
                writer.writerow([hotel_name, location, rating, score, review, link])

        print("✅ Web scraping completed. Data saved in:", f"{f_name}.csv")

    else:
        print(f"❌ Connection Failed! Status code: {response.status_code}")


if __name__ == '__main__':
    url = input("Please enter URL: ")
    fn = input("Please provide file name (without extension): ")
    web_scrapper2(url, fn)

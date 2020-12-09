# http://quotes.toscrape.com/

import csv
import requests

from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text, features = "html.parser")
quotes = html_data.find_all(class_='quote')

with open('my_file.csv', 'w', encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['text', 'author', 'content'])
    for quote in quotes:
        csv_writer.writerow([quote.find(class_='text').get_text(),
                             quote.find(class_='author').get_text(),
                             quote.find(class_='keywords')['content']])
# print(quote.find(class_='text').get_text())
# print(quote.find(class_='author').get_text())
# print(quote.find(class_='keywords')['content'])

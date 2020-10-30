#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

# Collect and parse first page
targeturl = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"  # noqa: E501
page = requests.get(targeturl)

soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

# For loop to print out artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

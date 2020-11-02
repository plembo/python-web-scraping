#!/usr/bin/env python
# Use requests to retrieve web page and parse with bs4.
# Page hosted by built-in python web server:
# python -m http.server 8888 --directory public/
from bs4 import BeautifulSoup
import requests as req

resp = req.get('http://localhost:8888')

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.title)
print(soup.body)

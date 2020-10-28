#!/usr/bin/env python
# Spruce up look of HTML code with the prettify method.
# Among others things, proper indents and spacing, which the
# original is missing.
from bs4 import BeautifulSoup
import requests as req

resp = req.get('http://webcode.me')

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.prettify())

#!/usr/bin/env python
# Tag name attribute gives tag name and text attribute its text content.
# Here, the attributes of the h2 tag are retrieved.
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(f'HTML: {soup.h2}, name: {soup.h2.name}, text: {soup.h2.text}')

#!/usr/bin/env python
# Use find_all with list of elements (<h2>, <p>)
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tags = soup.find_all(['h2', 'p'])

    for tag in tags:
        print(' '.join(tag.text.split()))

#!/usr/bin/env python
# Search and replace text ('Windows' with 'OpenBSD').
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tag = soup.find(text='Windows')
    tag.replace_with('OpenBSD')

    print(soup.ul.prettify())

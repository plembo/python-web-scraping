#!/usr/bin/env python
# Select element by css id tag (here, #mylist)
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select_one('#mylist'))
 
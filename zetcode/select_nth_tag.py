#!/usr/bin/env python
# Use css selector to find an element (in this case the
# third <li>)
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select('li:nth-of-type(3)'))

#!/usr/bin/env python
# Really simple first script. Import bs4 (BeautifulSoup), open the
# target file, and print the h2, head and li tags with their content.
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.h2)
    print(soup.head)
    print(soup.li)

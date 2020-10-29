#!/usr/bin/env python
# Use a function to determine what elements are returned
# (here, meta, the only empty elements)
from bs4 import BeautifulSoup


def myfun(tag):

    return tag.is_empty_element


with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tags = soup.find_all(myfun)
    print(tags)

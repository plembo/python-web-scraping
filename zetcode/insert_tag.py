#!/usr/bin/env python
# Insert a tag (here, between the existing first and second <li>)
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'

    ultag = soup.ul

    ultag.insert(2, newtag)

    print(ultag.prettify())

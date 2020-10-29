#!/usr/bin/python
# Remove a tag and destroy (decompose) it. Here, the 2nd <p> element.
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    ptag2 = soup.select_one('p:nth-of-type(2)')

    ptag2.decompose()

    print(soup.body.prettify())

#!/usr/bin/env python
# Find all the <li> tags. 
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for tag in soup.find_all('li'):
        print(f'{tag.name}: {tag.text}')

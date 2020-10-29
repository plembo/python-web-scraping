#!/usr/bin/env python
# Find elements by element id
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    #print(soup.find('ul', attrs={ 'id' : 'mylist'}))
    print(soup.find('ul', id='mylist'))

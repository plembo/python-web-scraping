#!/usr/bin/env python

from bs4 import BeautifulSoup

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(f'HTML: {soup.h2}, name: {soup.h2.name}, text: {soup.h2.text}')

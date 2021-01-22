# Get the links from an HTML file and print them with their labels
# to a csv file.
from bs4 import BeautifulSoup
import csv

with open('resources.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    writer.writerow(['Name', 'Link'])

    with open('wikipedia.html', 'r', encoding='utf-8') as f:

        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')

        all_links = soup.find_all('a', href=True)

        for link in all_links:
            hlink = link.get('href')
            hname = link.text
            writer.writerow([hname, hlink])

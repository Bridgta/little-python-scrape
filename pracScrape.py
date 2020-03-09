import bs4

import requests

res = requests.get('https://www.amazon.com/Bhagavad-Gita-2nd-Eknath-Easwaran/dp/1586380192/')

res.raise_for_status()

bs4.BeautifulSoup(res.text)

soup = bs4.BeautifulSoup(res.text)

soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
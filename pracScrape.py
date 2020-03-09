#commented code can be ran in terminal 

# import bs4

# import requests

# res = requests.get('https://www.amazon.com/Bhagavad-Gita-2nd-Eknath-Easwaran/dp/1586380192/')

# res.raise_for_status()

# bs4.BeautifulSoup(res.text)

# soup = bs4.BeautifulSoup(res.text)

# soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

# elems[0].text.strip()


import bs4, requests 

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    #should add a try/catch block or debugger break point for css updates 
    elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Bhagavad-Gita-2nd-Eknath-Easwaran/dp/1586380192/')
print(f'The cost is {price}')
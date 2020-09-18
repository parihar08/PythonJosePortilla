# Syntax                              Match Results
#
# soup.select('div')                  All elements with 'div' tag
# soup.select('#some_id')             Elements containing id = 'some_id'
# soup.select('.some_class')          Elements containing class = 'some_class'
# soup.select('div span')             Any elements named span within a div element
# soup.select('div > span')           Any elements named span directly within a div element
#                                     with nothing in between

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)  #Grabs entire content from the page

print('****************GRAB A CLASS************************','\n')
print(soup.select('.toctext'))  #Returns list of all spans associated with class toctext

print('****************************************')

first_item = soup.select('.toctext')[0]
print(first_item)               #<span class="toctext">Early life and education</span>

print('****************************************')

first_item_text = soup.select('.toctext')[0].text
print(first_item_text)          #Early life and education

print('**************GET TEXT OF ALL ITEMS**************************')

for item in soup.select('.toctext'):
    print(item.text)

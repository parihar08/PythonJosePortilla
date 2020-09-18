# WebScraping using Python:
# Using BeautifulSoup and requests libraries
# pip3 install requests
# pip3 install lxml
# pip3 install bs4

import requests
import bs4

result = requests.get('http://www.example.com')
print(type(result))     #<class 'requests.models.Response'>
#print(result.text)     #HTML Source code
print('***************SOUP OBJECT*************************','\n')

#In order to parse through this source code, we need Beautiful Soup library
#Converting raw string(result.text) to soup object(soup)
#Soup object is smart to be able to grab things based of their tags or elements
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

print('****************GRAB TITLE************************','\n')
print(soup.select('title'))     #Pass the element tag
#By default it returns a list, as there could be more than one tag or element on a page
#Output: [<title>Example Domain</title>]
print('****************************************')
print(soup.select('title')[0].getText()) #This returns back the actual Title text
#Output: Example Domain

print('****************GRAB PARAGRAPHS*******************','\n')
#Grab list of all paragraphs on the page
print(soup.select(('p')))
print('****************************************')
site_paragraphs = soup.select('p')
print(type(site_paragraphs))         #<class 'bs4.element.ResultSet'> --> BeautifulSoup Object
print(site_paragraphs[0].getText())  #Gives first paragraph

print('****************GRAB HEADERS*******************','\n')
#Grab list of all headers on the page
print(soup.select(('h1')))
print('****************************************')
site_headers = soup.select('h1')
print(type(site_headers))         #<class 'bs4.element.ResultSet'> --> BeautifulSoup Object
print(site_headers[0].getText())  #Gives first paragraph name - Example Domain




#Get the Title of Every book with a 2 star rating
#There are total 50 pages where books are listed. We need to get book title in all 1-50 pages

import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)  #Grabs entire content from the page

print(soup.select('.product_pod'))
print('****************************************')
print(len(soup.select('.product_pod')))     #20 items on page 1

print('****************************************')

products = soup.select('.product_pod')
example = products[0]
print(example)

print('****************************************')
#First way of checking if 2 star rating is present for a book using class value
print('star-rating Two' in str(example))

print('****************************************')
#Another way is by specifically checking if the class is present using Beautiful Soup

print(example.select('.star-rating.Two') )    #use . to fill out the space in class name

print('****************************************')
#Figure out how to grab title of the page

print(example.select('a')[1]['title'])

print('****************************************')
#We can check if something is 2 stars(string call in,example.select(rating))
#We can grab book title using example.select('a')[1]['title']

two_star_titles = []

for page_num in range(1,51):
    scrape_url = base_url.format(page_num)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')     #All books

    #Filter out 2 star books
    for book in books:
        #if 'star-rating.Two' in str(book):
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)

print('***********************************************************')

print('Number of Books having 2 star rating:',len(two_star_titles))

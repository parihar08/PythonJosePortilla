# Import libraries we need to scrape a website

import requests
import bs4

# Use request library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get HTML
#text from the homepage

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)                              #Grabs entire content from the page

# Get names of all the authors on the first page

print(soup.select('.col-md-8'))
print('****************************************')
print(len(soup.select('.col-md-8')))
print('****************************************')

quotes = soup.select('.col-md-8')
example = quotes[1]
print(example)

print('****************************************')

authors = example.select('.author')
print(authors)

print('**************First Author Name**************************','\n')
first_author = example.select('.author')[0]
print(first_author.text)

print('**************All Author Names on First Page**************************','\n')

for i in range(len(authors)):
    print(authors[i].text)

print('**************Distinct Author Names on First Page**************************','\n')

distinct_authors = set()

for i in range(len(authors)):
    all_authors = authors[i].text
    distinct_authors.add(all_authors)

print(distinct_authors)
print('****************************************')

# Get list of quotes on the first page
quotes = example.select('.text')
print(quotes)

print('**************List of All Quotes on First Page**************************','\n')

quotes_list = []
for i in range(len(quotes)):
    quotes_list.append(quotes[i].text)
print(quotes_list)
print('****************************************')
print(len(quotes_list))

print('***************All Quotes on First Page*************************','\n')

for i in range(len(quotes)):
    print(quotes[i].text)

print('****************************************')

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests
# text shown on the top right from the home page(e.g Love, Inspirational, Life etc.)

#HINT: Keep in mind there as also tags underneath each quote, try to find a class only present
# in the top right tags, perhaps check the span

tags = soup.select('.col-md-4.tags-box')
top_10_tags = tags[0]
print(top_10_tags)

print('****************************************')

tags_text = top_10_tags.select('.tag')
print(tags_text)
print('****************************************')
print(len(tags_text))

print('****************************************')
print(tags_text[0].text)

print('**************List Top 10 Tags on First Page**************************','\n')

tags_list = []
for i in range(len(tags_text)):
    tags_list.append(tags_text[i].text)

print(tags_list)

print('***************Top 10 Tags on First Page*************************','\n')

for i in range(len(tags_text)):
    print(tags_text[i].text,'\n')

print('****************************************')

# Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string
# concatenation to loop through all the pages and get all the unique authors on the website.
# Keep in mind there are many ways to achieve this, also note that you will need to somehow
# figure out how to check that your loop is on the last page with quotes. For debugging
# purposes, I will let you know that there are only 10 pages, so the last page is
# http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that
# it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this' \
# ',' \' its up to you!

base_url1 = 'http://quotes.toscrape.com/page/11/'
res = requests.get(base_url1)

soup = bs4.BeautifulSoup(res.text, 'lxml')
data = soup.select('.col-md-8')  # All data
example = data[1]
print('No quotes found!' in example.text)

print('****************************************')

base_url = 'http://quotes.toscrape.com/page/{}/'

all_authors = []
all_distinct_authors = set()
page_exist = True
page_num = 1

while page_exist:
    try:
        while page_num >= 1:
            scrape_url = base_url.format(page_num)
            res = requests.get(scrape_url)

            soup = bs4.BeautifulSoup(res.text, 'lxml')
            all_data = soup.select('.col-md-8')  # All data
            example = all_data[1]
            if 'No quotes found!' in example.text:
                page_exist = False
                break
            else:
                authors = example.select('.author')
                for i in range(len(authors)):
                    all_authors = authors[i].text
                    all_distinct_authors.add(all_authors)
                page_num += 1

        break

    except:
        print('No more pages \n')
        page_exist = False

print(all_distinct_authors)

print('***************ALTERNATE WAY*************************')

page_still_valid = True
authors = set()
page = 1

url = 'http://quotes.toscrape.com/page/'

while page_still_valid:
    page_url = url+str(page)
    res = requests.get(page_url)

    if 'No quotes found!' in res.text:
        break
    else:
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        for name in soup.select('.author'):
            authors.add(name.text)

    page = page + 1

print(authors)

# Images on websites typically have their own URL links ending with .jpg or .png
# Beautiful Soup can scan a page, locate the <img> tags and grab these URLs
# The we can download the URLs as images and write them to the computer

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)  #Grabs entire content from the page

print('****************GRAB AN IMAGE************************','\n')
print(soup.select('img'))  #Returns list of everything that has image tag associated

print('****************************************')

#Grab first image content
print(soup.select('img')[0])

print('****************************************')

#Grab images associated with the specific article of the page using class name
print(soup.select('.thumbimage'))

print('****************************************')

#Check out the image information
computer = soup.select('.thumbimage')[0]
print(computer)
#<img alt="" class="thumbimage" data-file-height="601" data-file-width="400"
# decoding="async" height="331" src="//upload.wikimedia.org/wikipedia/commons/thumb
# /b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg" srcset="//upload.wikimedia.org/wikipedia/
# commons/thumb/b/be/Deep_Blue.jpg/330px-Deep_Blue.jpg 1.5x, //upload.wikimedia.org/
# wikipedia/commons/b/be/Deep_Blue.jpg 2x" width="220"/>

print('****************************************')
#Type of computer is not a String, its a specialized Tag object
print(type(computer))       #<class 'bs4.element.Tag'>

print('****************************************')
#If we are looking for only one aspect, we can treat the output tag object as a dictionary
#We can do a call like a dictionary on tag object for any particluar part of this tag
print(computer['class'])        #['thumbimage']
print(computer['src'])          #//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg

print('***************DOWNLOADING THE IMAGE********************','\n')

#image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
image_link = requests.get('https:'+computer['src'])
#image_link.content      #Binary file of the image

f = open('my_computer_downloaded_image.jpg','wb')  #wb means binary writing
f.write(image_link.content)
f.close()

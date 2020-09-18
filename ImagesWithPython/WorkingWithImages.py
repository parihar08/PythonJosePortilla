# Working with Images using Python:
# Using pillow library which is an fork of PIL (Python Imaging Library) with easy to use function calls
# pip3 install pillow

#Official documentation at: pillow.readthedocs.io

from PIL import Image

mac = Image.open('ImagesWithPython/example.jpg')
print(type(mac))        #<class 'PIL.JpegImagePlugin.JpegImageFile'>
#To view the image
#mac.show()

print('*************IMAGE ATTRIBUTES****************','\n')

print(mac.size)                 #(1993, 1257)
print(mac.filename)             #ImagesWithPython/example.jpg
print(mac.format_description)   #JPEG (ISO 10918)

#IMAGE OPERATIONS
print('*************CROPPING IMAGES******************','\n')
cropped_image = mac.crop((0,0,100,100))   #Accepts a 4 item tuple (x,y,width,height) defining
                                          #the left,upper,right and lower pixel coordinate
cropped_image.show()

print('**********************************************')
pencils = Image.open('ImagesWithPython/pencils.jpg')
print(pencils.size)       #(1950, 1300)

#Grab pencils from the top
x = 0
y = 0
w = 1950/3
h = 1300/10

cropped_image = pencils.crop((x,y,w,h))
cropped_image.show()
print('**********************************************')
#Grab pencils from the bottom
x = 0
y = 1100
w = 1950/3
h = 1300

cropped_image = pencils.crop((x,y,w,h))
cropped_image.show()
print('**********************************************')
#Grab the computer from the halfway in the mac image
print(mac.size)                 #(1993, 1257)

halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

cropped_image = mac.crop((x,y,w,h))
cropped_image.show()

print('*************COPY IMAGES******************','\n')

#Copy image over another image
#This operation happens in memory, it doesn't permanently affect the original image
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box =(0,0))
mac.paste(im=computer,box =(796,0))  #Copying cropped image multiple times over original image
mac.show()

print('*************IMAGE RESIZE******************','\n')
print(mac.size)
resized_image = mac.resize((3000,500))
print(resized_image.size)
resized_image.show()

print('*************ROTATE IMAGES******************','\n')
rotated_image = mac.rotate(90)      #Rotate image by 90 degrees
rotated_image.show()

print('*************COLOR TRANSPARENCY******************','\n')
#RGBA - Red Green Blue Alpha
#All values for R,G,B,A can go from 0-255
#If Alpha value is 0:   Image is Transparent
#If Alpha value is 255: Image is Opaque

red = Image.open('ImagesWithPython/red_color.jpg')
red.show()

red_rgba1 = red.copy()
red_rgba1.putalpha(0)       #Transparent
red_rgba1.save('ImagesWithPython/red_transparent.png')  #Saving Image
red_rgba1.show()


red_rgba2 = red.copy()
red_rgba2.putalpha(255)     #Opaque
red_rgba2.save('ImagesWithPython/red_opaque.png')
red_rgba2.show()


red_rgba3 = red.copy()
red_rgba3.putalpha(128)     #Intermediate
red_rgba3.save('ImagesWithPython/red_intermediate.png')
red_rgba3.show()


blue = Image.open('ImagesWithPython/blue_color.png')
blue.show()

# These are giving some errors through Pycharm, Hence, commented for now.
# blue_rgba1 = blue.copy()
# blue_rgba1.putalpha(0)      #Transparent
# blue_rgba1.save('ImagesWithPython/blue_transparent.png')
# blue_rgba1.show()
#
# blue_rgba2 = blue.copy()
# blue_rgba2.putalpha(255)     #Opaque
# blue_rgba2.save('ImagesWithPython/blue_opaque.png')
# blue_rgba2.show()
#
# blue_rgba3= blue.copy()
# blue_rgba3.putalpha(128)     #Intermediate
# blue_rgba3.save('ImagesWithPython/blue_intermediate.png')
# blue_rgba3.show()

print('**********************************************')

#Paste one image over another (Merge 2 images of same size)
blue.paste(im=red_rgba3,box =(0,0),mask=red_rgba3)
blue.show()

# There are two images we will be working with:
# word_matrix.png
# mask.png

# The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it.

# Your task is to use the mask.png image to reveal the hidden message inside the word_matrix.png.
# Keep in mind, you may need to make changes to the mask.png in order for this to work. That is
# all we'll say for now, since we really want you to discover this on your own!

from PIL import Image

#Open Image
word_matrix = Image.open('ImagesWithPython/word_matrix.png')

mask = Image.open('ImagesWithPython/mask.png')

#Find Size of Images
print(word_matrix.size)     #(1015, 559)
print(mask.size)            #(505, 251)

#Re-Size the masked image to word_matrix images's size
resized_mask = mask.resize((1015,559))

word_matrix.show()
mask.show()
resized_mask.show()

#Use Color Transparency to set uniform transparency(128) across resized masked image
mask_rgba = resized_mask.copy()
mask_rgba.putalpha(128)       #Intermediate
mask_rgba.save('ImagesWithPython/mask_transparent.png')  #Saving Image
mask_rgba.show()

#Paste one image over another (Merge 2 images of same size)
word_matrix.paste(im=mask_rgba,box =(0,0),mask=mask_rgba)

#Save the final image
word_matrix.save('ImagesWithPython/word_matrix_solution.png')
#View the final image
word_matrix.show()

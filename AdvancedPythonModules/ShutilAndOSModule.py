#Opening and reading files and folders and performing actions on them such as moving or deleting
#How do we open every file in a directory
#How to move files around on our computer


f = open('practice.txt','w+')
f.write('This is test string')
f.close()

print('****************OS MODULE************************')

import os
print(os.getcwd())  #Returns current working directory
print('****************************************')

print(os.listdir()) #List everything in the current directory
print('****************************************')

print(os.listdir('/Users/Parihar08/PyCharmProjects'))
print('****************************************')

#Move files around
print('****************SHUTIL************************')

print('****************MOVING FILES************************')

import shutil
shutil.move('practice.txt','AdvancedPythonModules/')
#shutil.move('AdvancedPythonModules/practice.txt','../')
print(os.listdir('AdvancedPythonModules/'))

#Deleting a file
print('****************DELETING FILES************************')

#os.unlink(path)  #Deletes the file at the path specified
#os.rmdir(path)   #Deletes a folder(folder must be empty) at the path provided
#shutil.rmtree(path=) #Most dangerous. It will remove all the files and folders contained in the path

# Once files or folders are deleted, these can't be recovered
# Instead we can use send2trash module, which sends deleted files to trash bin instead of permanent removal

import send2trash

send2trash.send2trash('AdvancedPythonModules/practice.txt')
print(os.listdir('AdvancedPythonModules/'))

print('****************DIRECTORY TREE GENERATOR************************')
#os.walk - returns a tuple with folder, sub folder and files within it

file_path = '/Users/Parihar08/PycharmProjects/PythonJosePortilla/MilestoneProject2'
for folder,subfolders,files in os.walk(file_path):
    print(f'Currently looking at: {folder}')
    print('\n')
    print('The Sub-Folders are: ')
    for sub_fold in subfolders:
        print(f'\t SubFolder: {sub_fold}')
    print('\n')
    print('The Files are: ')
    for f in files:
        print(f'\t Files: {f}')
    print('\n')
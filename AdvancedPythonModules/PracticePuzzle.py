#There is a zipfile called unzip_me_for_instructions.zip, unzip it and open the .txt file,
#Read out the instructions and figure out what needs to be done

# import shutil
#
# shutil.unpack_archive('ZipPracticePuzzle/unzip_me_for_instructions.zip','ZipPracticePuzzle/','zip')

with open('ZipPracticePuzzle/extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

print('*********************************************')

import re

pattern1 = r'\d{3}-\d{3}-\d{4}'
test_string = 'Here is a phone number 123-123-1234'
print(re.findall(pattern1,test_string))

def search(file,pattern=pattern1):
    f = open(file,'r')
    text = f.read()
    #Open a file, look for a pattern, if it finds it, return the pattern
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

import os

results = []
for folder, subfolders,files in os.walk(os.getcwd()+'/ZipPracticePuzzle/extracted_content'):
    for f in files:
        full_path = folder+'/'+f
        print(full_path)

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r)
        print(r.group())

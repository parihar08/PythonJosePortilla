# We will need to work with two files for this exercise and solve the following tasks:
#
# Task One: Use Python to extract the Google Drive link from the .csv file.
#           (Hint: Its along the diagonal from top left to bottom right).
# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you
#           just in case you can't download from Google Drive) and find the phone number that
#           is in the document. Note: There are different ways of formatting a phone number!
print('*****************TASK 1************************','\n')

import csv

#Open the file
data = open('PDFAndSpreadsheetCSVFiles/Exercise_Files/find_the_link.csv',encoding='utf-8')

#Call csv.reader
csv_data = csv.reader(data)

#Reformat it into a python object - list of lists
data_lines = list(csv_data)

print('Number of ROWS in CSV File:',len(data_lines))

print('***********************************************')

link = []
i = 0
for line in data_lines[:len(data_lines)]:
    link.append(line[i])
    i +=1

print(link)
print('***********************************************')

#URL Extracted is:
print('Extracted URL is:',''.join(link))

print('*****************ANOTHER WAY******************************','\n')

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)

print('*****************TASK 2************************','\n')

import PyPDF2

f = open('PDFAndSpreadsheetCSVFiles/Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print('Number of Pages:',pdf_reader.numPages)

print('***********************************************')
import re

pattern = r'\d{3}'
all_text = ''

for num in range(pdf_reader.numPages):

    page = pdf_reader.getPage(num)
    page_text = page.extractText()
    all_text = all_text +' '+ page_text

print(all_text)     #String containing all text of pdf file

print('***********************************************')

print(re.findall(pattern,all_text))     #['000', '000', '000', '505', '503', '445']

print('***********************************************')

for match in re.finditer(pattern,all_text):
    print(match)
# Output:
# <re.Match object; span=(655, 658), match='000'>
# <re.Match object; span=(17805, 17808), match='000'>
# <re.Match object; span=(35059, 35062), match='000'>
# <re.Match object; span=(41808, 41811), match='505'>
# <re.Match object; span=(41812, 41815), match='503'>
# <re.Match object; span=(41816, 41819), match='445'>

print('***********************************************')

print(all_text[41808:41811+20])     #505.503.4455. So horseh

print('***********************************************')

#We do not need 20 extra characters, we only need 9 extra characters from first 3 digits of phone number

print(all_text[41808:41811+9])      #505.503.4455
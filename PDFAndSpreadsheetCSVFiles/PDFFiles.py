# PDF - Portable Document Format
# Many PDFs are not machine readable through python

# Working with PDF Files using Python:
# Using PyPDF2 library: pip3 install PyPDF2

import PyPDF2

f = open('PDFAndSpreadsheetCSVFiles/Working_Business_Proposal.pdf','rb') #Read Binary

pdf_reader = PyPDF2.PdfFileReader(f)

print('*************No OF PAGES IN PDF****************','\n')
print('Number of Pages:',pdf_reader.numPages)

print('*************PRINT TEXT OF FIRST PAGE IN PDF****************','\n')
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)    #Returns text as Python String

f.close()

print('*************ADD PAGES TO END OF A PDF FILE****************','\n')

f = open('PDFAndSpreadsheetCSVFiles/Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)
print(type(first_page))         #<class 'PyPDF2.pdf.PageObject'>

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)

#This will overwrite current existing binary pdf file if we have it
pdf_output = open('PDFAndSpreadsheetCSVFiles/Some_BrandNew_Doc.pdf','wb')

#Write page1 of Business PDF file to SomeBrandNewDoc pdf file
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

print('*************GRAB ALL TEXT WITHIN A PDF FILE****************','\n')

f = open('PDFAndSpreadsheetCSVFiles/Working_Business_Proposal.pdf','rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text)     #Prints all pages text
print('****************************************','\n')
print(pdf_text[0])  #Print first page text

import csv

#Open the file
data = open('PDFAndSpreadsheetCSVFiles/example.csv',encoding='utf-8')

#Call csv.reader
csv_data = csv.reader(data)

#Reformat it into a python object - list of lists
data_lines = list(csv_data) #Might give UnicodeDecodeError without encoding
#print(data_lines)       #List of lists [[],[],[]]

print(data_lines[0])    #First Line contains the column names
#Output: ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']

print('**********************************************')

print('Number of ROWS in CSV File:',len(data_lines))    #1001 - 1 of them is column name

print('**********************************************')

for line in data_lines[:5]:
    print(line)             #Prints first 5 lines (0-4)

print('*************EXTRACT A ROW****************','\n')

print(data_lines[10])    #Tenth Data Line (as column name is at 0 index)

#Extact attribute from a specific row

print('Email is:',data_lines[10][3])

print('************EXTRACT ALL VALUES FROM A COLUMN****************','\n')
#Extract all email values from email columns (for 15 rows)

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

print('************MERGE VALUES OF 2 COLUMNS****************','\n')
#Get full name using first name and last name column value
print(data_lines[10])

print('**********************************************')
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])
print(full_names)

print('************WRITE TO A CSV FILE****************','\n')

file_to_output = open('PDFAndSpreadsheetCSVFiles/to_save_file.csv',mode='w',newline='')
#Overrides existing csv file with the same name

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])  #Add single row

csv_writer.writerows([['1','2','3'],['4','5','6']]) #Takes list of lists

file_to_output.close()

print('************APPEND THE CSV FILE****************','\n')

f = open('PDFAndSpreadsheetCSVFiles/to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['7','8','9'])
csv_writer.writerows([['10','11','12'],['13','14','15']])

f.close()
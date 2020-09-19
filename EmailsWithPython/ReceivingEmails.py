# To view received emails with Python, we can use the builtin
# imaplib and email libraries in Python

# The imaplib library has a special syntax for searching your inbox

print('**********VIEWING EMAILS***************','\n')

import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

#Secure way to pass information
#email = getpass.getpass('Email: ')
email = 'pariindiana88@gmail.com'
password = getpass.getpass('Password: ')

#Login
M.login(email,password)
print(M.list())

print('*********************************','\n')

M.select('inbox')

#type, data = M.search(None,'FROM pariindiana88@gmail.com')
type, data = M.search(None,'SUBJECT "Test Email through Python Script"')

print(type)
print('*********************************','\n')
print(data)     #Some number ID is returned, means it found the data
print('*********************************','\n')

email_id = data[0]

result, email_data = M.fetch(email_id,'(RFC822)')
print(email_data)       #Returns list of tuples

print('*********************************','\n')

raw_email = email_data[0][1]    #Since email data is at index 1 of tuple within the data list
raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)

print('*********************************','\n')

import email
#import library helps grab the actual message from the string

email_message = email.message_from_string(raw_email_string)
print(email_message)        #Its an iterator
print('*********************************','\n')

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':     #Use 'text/html': for links
        body = part.get_payload(decode=True)
        print(body)

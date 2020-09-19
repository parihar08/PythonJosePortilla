# Steps:
# 1. Connect to an email server
# 2. Confirming connection
# 3. Setting Protocol
# 4. Logging on
# 5. Sending the message

#Built-in smtplib library is used for sending/receiving emails with Python

# Provider	                        SMTP server domain name
# Gmail (will need App Password)	smtp.gmail.com (Use port 587 or 465 or No Port)
# Yahoo Mail	                    smtp.mail.yahoo.com
# Outlook.com/Hotmail.com	        smtp-mail.outlook.com
# AT&T	                            smpt.mail.att.net (Use port 465)
# Verizon	                        smtp.verizon.net (Use port 465)
# Comcast	                        smtp.comcast.net

import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()

smtp_object.starttls()      #if using Port 465, skip this step as we will be using SSL

import getpass

#Secure way to pass information
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

#Generate an app password for Gmail - Turn on 2 step verification

#Login
smtp_object.login(email,password)

from_address = email
to_address = email              #or we can use 'sparihar08@yahoo.com'
subject = input('Enter the Subject line: ')
message = input('Enter the body message: ')

msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()
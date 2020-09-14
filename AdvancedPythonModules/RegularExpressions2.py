print('****************CHARACTER IDENTIFIERS******************','\n')

# Character   Description             Example Pattern Code            Example Match
# \d          A digit                 file_\d\d                       file_25
# \w          Alphanumeric            \w-\w\w\w                       A-b_1
# \s          White space             a\sb\sc                         a b c
# \D          A non-digit             \D\D\D                          ABC
# \W          Non-alphanumeric        \W\W\W\W\W                      *-+=)
# \S          Non-whitespace          \S\S\S\S                        Yoyo

import re

text = 'My phone number is 408-555-1234'
phone = re.search('408-555-1234',text)
print(phone)        #<re.Match object; span=(19, 31), match='408-555-1234'>
print('*********************************************')

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)        #<re.Match object; span=(19, 31), match='408-555-1234'>
print(phone.group())#408-555-1234

print('****************CHARACTER QUANTIFIERS******************','\n')
# Character     Description               Example Pattern Code      Example Match
# +             Occurs one or more time   Version \w-\w+            Version A-b1_1
# {3}           Occurs exactly 3 times    \D{3}                     abc
# {2,4}         Occurs 2 to 4 times       \d{2,4}                   123
# {3,}          Occurs 3 or more          \w{3,}                    anycharacters
# *             Occurs 0 or more times    A*B*C*                    AAACC
# ?             Once or None              plurals?                  plural

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)        #<re.Match object; span=(19, 31), match='408-555-1234'>
print(phone.group())#408-555-1234

print('*****************COMPILE()-->GROUP()****************************')
#Extract the area code - first 3 digits of the phone
#re.compile() -> compiles together different regular expression pattern codes
#Each pattern code is separated by parenthesis as a group and compiles into a single expression
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())      #408-555-1234

print('****************GROUP ORDERING*****************************')
#We can call each pattern code by the group position. Group ordering starts at 1
print(results.group(1))     #408
print(results.group(2))     #555
print(results.group(3))     #1234
#print(results.group(4))    #IndexError: no such group

print('*********************************************')


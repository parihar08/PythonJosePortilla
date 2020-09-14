#Pattern Structure of the string we are looking for - like email or phone number
#Regular Expressions(regex) allow us to search for general patterns in text data
#Email: user@email.com
#Pattern: 'text' + '@' + 'text' + '.com'

print('****************re Library******************','\n')
#Phone Number: (555)-555-5555
#Regex Pattern: r"(\d\d\d)-\d\d\d-\d\d\d\d"     #\d -> digits
#Regex Pattern: r"(\d{3})-\d{3}-\d{4}"          #\d -> digits

text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)
print('*********************************************')

import re
pattern = 'phone'
print(re.search(pattern,text))  #<re.Match object; span=(12, 17), match='phone'>
print('*********************************************')

pattern = 'NOT IN TEXT'
print(re.search(pattern,text))  #None -> no match (no pattern is found)

print('*****************MATCH****************************')

pattern = 'phone'
match = re.search(pattern,text)
print(match)            #<re.Match object; span=(12, 17), match='phone'>
print(match.span())     #(12,17)  -> Gives the index location of the match
print(match.start())    #12
print(match.end())      #17

#If there are multiple matches, we only get back the first match
text = 'my phone once, my phone twice'
pattern = 'phone'
match = re.search(pattern,text)
print(match)            #<re.Match object; span=(3, 8), match='phone'>

print('*****************TO FIND MULTIPLE MATCHES - FINDALL****************************')

matches = re.findall(pattern,text)
print(matches)      #['phone ', 'phone'] -> Returns the list of matches
print(len(matches)) #2

print('*****************FINDITER--->MATCH************************')
#To get back actual match object
for match in re.finditer('phone',text):
    print(match)

# Output:
# <re.Match object; span=(3, 8), match='phone'>
# <re.Match object; span=(18, 23), match='phone'>

print('*****************FINDITER--->MATCH.SPAN()****************************')
#To get back actual match span
for match in re.finditer('phone',text):
    print(match.span())

# Output:
# (3, 8)
# (18, 23)

print('*******************FINDITER--->MATCH.GROUP()**************************')
#To get back actual text that matched
for match in re.finditer('phone',text):
    print(match.group())

# Output:
# phone
# phone


print('****************ADDITIONAL REGEX SYNTAX******************','\n')

import re

print(re.search(r'cat','The cat is here'))      #<re.Match object; span=(4, 7), match='cat'>

print('****************OR OPERATOR******************','\n')
#Search cat OR dog using | operator
print(re.search(r'cat|dog','The dog is here'))  #<re.Match object; span=(4, 7), match='dog'>
print(re.search(r'cat|dog','The cat is here'))  #<re.Match object; span=(4, 7), match='cat'>

print('*****************WILDCARD OPERATOR .*******************','\n')

print(re.findall(r'at','The cat in the hat sat there.'))        #['at', 'at', 'at']

#What if we want to grab actual letter in front of at
print(re.findall(r'.at','The cat in the hat sat there.'))       #['cat', 'hat', 'sat']

print(re.findall(r'...at','The cat in the hat went splat.'))     #['e cat', 'e hat', 'splat']

print('*****************^ STARTS WITH*******************','\n')
#Search for a string starting with a digit
print(re.findall(r'^\d','1 is a number'))       #['1']

print(re.findall(r'^\d','The 2 is a number'))   #[] -> We won't get anything here

print('*****************ENDS WITH $*******************','\n')
#Search for a string that ends with a digit
print(re.findall(r'\d$','The number is 2'))       #['2']
print(re.findall(r'\d$','2 is a number'))     #[] -> We won't get anything here

print('*****************[^] GROUPING FOR EXCLUSION*******************','\n')

#Get back everything that isn't a number in the string - Exclude digits
phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'  #Exclude digits
print(re.findall(pattern,phrase))

#Output: List of all characters that isn't a number
#['T', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's',
#  ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'n',
#  't', 'e', 'n', 'c', 'e']
print('*********************************************')

#To get the words back together
pattern1 = r'[^\d]+'
print(re.findall(pattern1,phrase))
#Output: We get back list split on any numbers
#['There are ', ' numbers ', ' inside ', ' this sentence']
print('*********************************************')

#Exclusions are very good way to get rid of punctuation from a sentence
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.?]+',test_phrase))
#Output: We get back list split on ! . ?
#['This is a string', ' But it has punctuation', ' How can we remove it']
print('*********************************************')

#Added a space as well
print(re.findall(r'[^!.? ]+',test_phrase))
#Output: We get back list of all the words
#['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we',
# 'remove', 'it']
print('*********************************************')

clean = re.findall(r'[^!.? ]+',test_phrase)
print(' '.join(clean))      #This is a string But it has punctuation How can we remove it

print('*****************GROUPING FOR INCLUSION*******************','\n')

text = ' Only find the hypen-words in the sentence. But you do not know how long-ish they are'
pattern = r'[\w]+'
print(re.findall(pattern,text))
#Output: This will find any grouping of alphanumeric
#['Only', 'find', 'the', 'hypen', 'words', 'in', 'the', 'sentence', 'But', 'you', 'do',
# 'not', 'know', 'how', 'long', 'ish', 'they', 'are']
print('*********************************************')

#To find hyphenated words
pattern1 = r'[\w]+-[\w]+'
print(re.findall(pattern1,text))    #['hypen-words', 'long-ish']
print('*********************************************')

#We can also remove brackets and find hyphenated words
pattern2 = r'\w+-\w+'
print(re.findall(pattern2,text))    #['hypen-words', 'long-ish']
print('*********************************************')

print('*****************PARENTHESIS FOR MULTIPLE OPTIONS*******************','\n')

text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar?'
#Last word all of these starts with cat
print(re.search(r'cat(fish|nap|claw)',text))        #<re.Match object; span=(27, 34), match='catfish'>
print(re.search(r'cat(fish|nap|claw)',texttwo))     #<re.Match object; span=(32, 38), match='catnap'>
print(re.search(r'cat(fish|nap|claw)',textthree))   #None --> as fish, nap or claw isn't in textthree
print(re.search(r'cat(fish|nap|erpillar)',textthree)) #<re.Match object; span=(26, 37), match='caterpillar'>

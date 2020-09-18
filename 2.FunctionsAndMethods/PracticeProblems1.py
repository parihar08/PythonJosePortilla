#Write a program that capitalizes first and fourth character of a word

print('**************Using Upper()**********************')
def old_mcdonald(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + in_between + fourth_letter.upper() + rest

print(old_mcdonald('macdonald'))

print('**************Using Capitalize()**********************')

def old_mcdonald1(name):
    first_part = name[:3]
    second_part = name[3:]
    return first_part.capitalize() + second_part.capitalize()

print(old_mcdonald1('macdonald'))

print('************************************')

#MASTER YODA, Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    list = text.split()
    reverse_list = list[::-1]
    return ' '.join(reverse_list)

print(master_yoda('This is an example of reversing words in a sentence'))

print('************************************')

#Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
     return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print(almost_there(211))

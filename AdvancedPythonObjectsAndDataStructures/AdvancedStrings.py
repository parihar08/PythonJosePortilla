s = 'hello world'

print('*********CHANGING CASE************','\n')

print(s.capitalize())
print(s.lower())
print(s.upper())

print('*********LOCATION AND COUNTING************','\n')

print(s.count('o'))

#Find first occurrence/index of 'o'
print(s.find('o'))

print('*********FORMATTING************','\n')

#Centre hello world between zzzz and total length of string is 20
print(s.center(20,'z'))             #zzzzhello worldzzzzz

print('*********EXPAND TABS************','\n')

print('hello\thi')                  #hello   hi
print('hello\thi'.expandtabs())     #hello   hi

print('*********IS CHECK METHODS************','\n')

s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isupper())
print('HELLO'.isupper())
print(s.endswith('o'))

print('*********BUILT-IN REGULAR EXPRESSIONS************','\n')

s = 'hello'
print(s.split('e'))     #['h', 'llo'] Split splits at every instance

s = 'hihihhihihhihi'
print(s.split('i'))     #['h', 'h', 'hh', 'h', 'hh', 'h', '']

print(s.partition('i')) #('h', 'i', 'hihhihihhihi') partition splits at first instance
                        # and also returns separator in the middle ('i')

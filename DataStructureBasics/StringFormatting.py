#https://pyformat.info/
#String Formatting

#1. format() method
#2. f-strings (formatted string literals)  for newer versions of Python3 (3.6)

print('This is a string {}'.format('INSERTED'))
print('This {} {} {}'.format('fox','brown','quick'))
print('This {2} {1} {0}'.format('fox','brown','quick'))
print('This {0} {0} {0}'.format('fox','brown','quick'))
print('This {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
print('This {f} {f} {f}'.format(f='fox',b='brown',q='quick'))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('11','22','33'))
print('************************************')

#Float Formatting
result= (100/777)
print('The result was {}'.format(result))
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))  #1.3f means 1 width 3 is the precision of decimal place
print('The result was {r:10.5f}'.format(r=result))
print('************************************')

#String literals
name = "Sandeep"
age = 29
print('Hello his name is {}'.format(name))
print(f'Hello his name is {name}')  #String Literal
print(f'Hello his name is {name} and is {age} years old')
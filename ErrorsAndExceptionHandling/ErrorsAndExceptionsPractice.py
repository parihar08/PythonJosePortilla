#1. Handle the exceptions thrown by below code

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('There is an Type Exception!!')
finally:
    print("Let's fix the problem and run again")

print('***********************************************************')

#2. Handle the exceptions thrown by below code and use finally to print All Done
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('There is a Zero Division Error!!')
finally:
    print('All Done')

print('***********************************************************')

#3. Write a function that asks for integer and prints square of it. Use a while loop and
#a try, except and else block to account for incorrect input

waiting = True
while waiting:
    try:
        num = int(input('Please enter the number: '))
        square = num**2
    except:
        print('Please enter the correct input!! \n')
        continue
    else:
        waiting = False
print('Thank you, Square of the number is: {}'.format(square))
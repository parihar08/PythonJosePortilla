#We can use Error Handling to let the script continue with other code, even if there is an error
#Keywords: try catch finally

def add(n1,n2):
    print(n1+n2)

add(10,20)

num1 = 10
#num2 = input('Please provide the input: ')
#add(num1,num2) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

print('******************TRY EXCEPT ELSE**********************************')

try:
    #WANT TO ATTEMPT THE CODE WHICH MAY HAVE ERROR
    result = 20+'30'
    print('TRY- Add went well')
except:
    print("EXCEPT- Hey! it looks like you aren't adding correctly!")
else:
    #In case there is no error, execute below
    print('ELSE- Add went well')
    print(result)

print('******************TRY EXCEPT FINALLY**********************************')

try:
    #WANT TO ATTEMPT THE CODE WHICH MAY HAVE ERROR
    result = 20+'30'
except:
    print("EXCEPT- Hey! it looks like you aren't adding correctly!")
finally:
    #In case there is no error, execute below
    print('FINALLY- This is executed irrespective of any error in try block')
    print('FINALLY- Add went well')

print('******************TRY EXCEPT FINALLY**********************************')

try:
    #f = open('testfile','w')
    f = open('testfile', 'r') #Open file in read mode and try writing to it - OS Error
    f.write('Write a test line')
except TypeError:
    print('There was a Type Error')
except OSError:
    print('Hey! you have an OS Error')
except:
    print('All other exceptions')
finally:
    print('I always run!')

print('***********************************************************')

def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes! Thank you..')
            break
        finally:
            print("I'm going to ask you again!!")

ask_for_int()
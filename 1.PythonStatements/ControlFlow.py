#https://github.com/Pierian-Data/Complete-Python-3-Bootcamp

#ControlFlowStatements makes use of indentation and white spaces

if True:
    print('Its True!!!')

if 3 > 2:
    print('Its True!!!')

print('****************************************************')

hungry = False
if hungry:
    print('Feed Me!!!')
else:
    print("I'm Full!!!")

print('****************************************************')

loc = "Bank"
if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the store!")
else:
    print("I do not know much.")

print('****************************************************')

#FizzBuzz
for i in range(1,101):
    if i%3 == 0 and i%5==0:
        print('FizzBuzz')
    elif i%3 ==0:
        print('Fizz')
    elif i%5 ==0:
        print('Buzz')
    else:
        print(i)

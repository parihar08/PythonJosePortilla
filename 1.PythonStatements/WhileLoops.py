#While loop will continue to execute a block of code while some condition remains True

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x+1
else:
    print('X IS NOT LESS THAN 5')

#Break:     Breaks out of the current closest enclosing loop
#Continue:  Goes to the top of the closest enclosing loop
#Pass:      Does nothing at all (users used to avoid syntax errors)

print('***************Pass*******************')
y = [1,2,3]
for item in y:
    pass
print('End of the script!')

print('***************Continue*******************')
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue       #Skips letter 'a' and go back to the loop. O/p: S m m y
    print(letter)

print('***************Break*******************')
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        break       #Prints only letter 'S' and breaks out of the loop. O/p: S
    print(letter)

print('***************BreakWithWhile*******************')
x = 0
while x < 5:
    if x == 2:
        break
    print(f'The current value of x is {x}')
    x = x+1
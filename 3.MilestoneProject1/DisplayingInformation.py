def display1(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

example_row1= [1,2,3]
example_row2= [4,5,6]
example_row3= [7,8,9]

display1(example_row1,example_row2,example_row3)

print('****************************************')

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1= [' ',' ',' ']
row2= [' ',' ',' ']
row3= [' ',' ',' ']

display(row1,row2,row3)
print('****************************************')
row2[1] = 'X'
display(row1,row2,row3)

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1= [' ',' ',' ']
row2= [' ',' ',' ']
row3= [' ',' ',' ']

position_index = int(input('Choose an index position: '))
result = input('Please enter a value: X or O - ')

#print('****************************************')
#row2[position_index] = result
#display(row1, row2, row3)
print('****************************************')
while result not in('X','O'):
    print('Please enter the correct value: X or O')
    result = input('Please enter a value: X or O - ')
if result in('X','O'):
    row2[position_index] = result
    display(row1, row2, row3)

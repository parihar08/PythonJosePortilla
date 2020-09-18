# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
# row1= [' ',' ',' ']
# row2= [' ',' ',' ']
# row3= [' ',' ',' ']
#
# position_index = int(input('Choose an index position: '))
# result = input('Please enter a value: X or O - ')
#
# print('****************************************')
# while result not in('X','O'):
#     print('Please enter the correct value: X or O')
#     result = input('Please enter a value: X or O - ')
# if result in('X','O'):
#     row2[position_index] = result
#     display(row1, row2, row3)

print('****************************************')

#User can pass in something that isn't a digit
#User can pass in something out of the required range
def user_choice():
    acceptable_range = range(0,11)
    choice = input('Please enter a number (0-10): ')
    #print(choice)
    while choice.isdigit():
        if int(choice) not in acceptable_range:
            print(f'Sorry, {choice} is not in a acceptable range (0-10)')
            #print(choice)
            user_choice()
            break
        else:
            print(f'{choice} is a number in acceptable range')
            return int(choice)
    if choice.isdigit()==False:
        print(f'Sorry, {choice} is not a digit')
        user_choice()


user_choice()
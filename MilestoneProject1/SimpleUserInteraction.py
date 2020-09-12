# Display a list
# Have a user choose an index position and an input value
# Replace value at index position with user's chosen input value

game_list = [0,1,2]

def display_game(game_list):
    print("Here's the current list: ")
    print(game_list)

#display_game(game_list)

def position_choice():
    #This is original choice which can be anything that is not an integer
    choice = 'wrong'
    #While the choice is not an integer, keep asking for an input
    while choice not in ['0','1','2']:
        #We should not convert here, otherwise we get an error on wrong input
        choice = input('Pick a position to replace (0,1,2): ')
        if choice not in ['0','1','2']:
            #This clears the current output below the cell
            #clear_output()
            print("Sorry but you didn't choose a valid position (0,1,2) ")
    #We can convert once the while loop above has confirmed we have a digit
    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input('Type a string to place the position: ')
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    #This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    # While the choice is not a digit, keep asking for an input
    while choice not in ['Y','N']:
        # We should not convert here, otherwise we get an error on wrong input
        choice = input('Would you like to keep playing? Y or N: ')
        if choice not in ['Y','N']:
            print("Sorry I didn't understand. Please make sure you choose Y or N ")
    if choice == 'Y':
        #Game is still on
        return True
    else:
        #Game is over
        return False

#Variable to keep game playing
game_on = True

#First Game List
#game_list = [0,1,2]

while game_on:
    display_game(game_list)
    #Have a player choose a position
    position = position_choice()
    #Rewrite the position and update game list
    game_list = replacement_choice(game_list,position)
    #Show updated game list
    display_game(game_list)
    #Ask if you want to keep playing
    game_on = gameon_choice()











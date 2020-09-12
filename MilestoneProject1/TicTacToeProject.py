#Step1:
#Setup your board as a list, where each index 1-9 corresponds with a number on number pad
#so we get 3*3 representation

def display_board(board):
    print('\n'*100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])

#test_board1 = (['#','X','0','X','0','X','0','X','0','X'])
#test_board = ([' ']*10) #Emply board initially
#display_board(test_board)

#Step2
#Write a function that can take in a player input and assign their marker as 'X' or 'O'.
#Think about using loops to continually ask until you get correct answer

def player_guess():
    """
    Output: (player1 marker, player2 marker)

    """
    marker = ''
    while marker not in ['X','O']:
        # We should not convert here, otherwise we get an error on wrong input
        marker = input('Player 1,Choose X or O: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2) #Assin them to a tuple

#print(player_guess())

#Step3:
#Write a function that takes in the board list object, a market ('X' or 'O') and a desired
#position number(1-9) and assigns it to the board

def place_marker(board,marker,position):
    board[position] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

#Step4:
#Write a function that takes in a board and marks (X or O) and then checks to see if that
#mark has won

def win_check(board,mark):

    #WIN TIC TAC TOE
    #All ROWS, and check to see if they all share the same marker?
    # All COLUMNS, and check to see if they all share the same marker?
    # All DIAGONALS, and check to see if they all share the same marker?
    return(
    (board[1] == mark and board[2] == mark and board[3] == mark) or #Row1
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Row2
    (board[7] == mark and board[8] == mark and board[9] == mark) or #Row3
    (board[8] == mark and board[5] == mark and board[2] == mark) or #Col1
    (board[9] == mark and board[6] == mark and board[3] == mark) or #Col2
    (board[7] == mark and board[4] == mark and board[1] == mark) or #Col3
    (board[9] == mark and board[5] == mark and board[1] == mark) or #Diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark))   #Diagonal

# display_board(test_board1)
# print(win_check(test_board1,'X'))

#Step5
#Write a function that used random module to randomly decide which player goes first.
#Return a string of which player went first

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Step6
#Write a function that returns a boolean indicating whether a space on the
#board is freely available

def space_check(board,position):
    return board[position] == ' '

#Step7
#Write a function that checks if the board is full and returns a boolean
#True if full, False otherwise

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #BOARD IS FULL IF WE RETURN TRUE
    return True

#Step8
#Write a function that asks for player's next position(1-9) and then uses the function
#from Step6 to check if it is a free position. If it is, then return the position for
#later use

def player_choice(board,turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(turn+' Choose a position: (1-9): '))
    return position

#Step9
#Write a function that asks if a player if they want to play again and returns a
#boolean True if they want to play again

def replay():
    choice = input('Play again? Enter Yes or No: ')
    return choice == 'Yes'

#Step10
#Write a function that uses while loops and functions to run the game


#WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')
while True:
    #PLAY THE GAME
    #SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS)
    the_board = [' ']*10
    player1_marker, player2_marker = player_guess()  #Tuple unpacking
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N? ')

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #GAME PLAY
    while game_on:
        # PLAYER1 TURN
        if turn == 'Player 1':
            #Show the board
            display_board(the_board)
            #Choose a position
            position =player_choice(the_board,turn)
            #Place the marker on the position
            place_marker(the_board,player1_marker,position)
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            # or Check if their is tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                # No tie or no win? Then next player's turn
                else:
                    turn = 'Player 2'

        # PLAYER2 TURN
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board,turn)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            # or Check if their is tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                # No tie or no win? Then next player's turn
                else:
                    turn = 'Player 1'

    # BREAK OUT OF WHILE LOOP ON REPLAY()
    if not replay():
        break


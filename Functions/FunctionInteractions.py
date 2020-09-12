#Shuffle a list at random

from random import shuffle

example = [1,2,3,4,4,5,6,7]
shuffle(example)
print(example)

#Create function to shuffle list

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)
print('************************************')

#Game list

#Setup Initial List
gamelist= ['','O','']

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0, 1 or 2 : ")

    return int(guess)

#player_guess()

def check_guess(gamelist,guess):
    if gamelist[guess]=='O':
        print("Hurray!! You Rock^^^")
        print(gamelist)
    else:
        print('Better luck next time!!!')
        print(gamelist)

#Shuffle List
mixedup_list=shuffle_list(gamelist)

#User Guess
guess = player_guess()

#Check Guess
check_guess(mixedup_list,guess)





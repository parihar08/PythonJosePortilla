#CARD class has 3 properties - SUITE RANK VALUE
#Should be able to understand Suite of the card - Heart/Diamond/Spades/Club
#Should be able to understand Rank of the card - 2-10/Jack/Queen/King/Ace
#Should be able to understand integer value corresponding Rank of the card

#Step1: Global variables
# Import random module. This will be used to shuffle the deck prior to dealing. Then declare
# variables to store suits, ranks and values. Finally declare a boolean value to be used to
# control while loops

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Club') #Set as Tuple
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
          'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') #Set as Tuple
#Create a dictionary for Card rank and their values
#Face Cards (Jack, Queen, King) count as a value of 10
#Aces can count as either 1 or 11 whichever value is preferable to the player
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#Step2:
# Create a Card Class. A Card object really needs two attributes: suit and rank
# In addition to the __init__ method, consider adding a __str__ method, that when asked
# to print a card, returns a String in the form - Two of Hearts.

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self. rank = rank

    def __str__(self):
        return self.rank+ " of "+self.suit

#Step3:
# Create a Deck Class. We can store 52 card objects in a list that can later be shuffled.
# First we need to instantiate all 52 unique card objects and add them to our list.

class Deck():

    def __init__(self):
        self.deck = [] #start with an empty list
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)

                self.deck.append(created_card) #self.deck is list of card objects

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp #This will give list of all cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card #Pop of a card object

new_deck1 = Deck()
print('************LIST OF ALL CARDS IN DECK************************')
#Prints all 52 card objects e.g. Two of Hearts, Ace of Clubs, Seven of Spades, King of Diamonds
for card_object in new_deck1.deck:
    print(card_object)

print('*************CARDS SHUFFLED***********************')

#Shuffling the cards and checking which one is the top and bottom card
new_deck2 = Deck()
new_deck2.shuffle()
print('Top Card: ',new_deck2.deck[0])
print('Bottom Card: ',new_deck2.deck[-1])

print('***************GRAB A CARD FROM SHUFFLED DECK*********************')
#Shuffling the cards and grab one from the deck of cards
new_deck3 = Deck()
new_deck3.shuffle()
print(new_deck3)
my_card = new_deck3.deal()
print('My Card: ',my_card)

print('***************HAND*********************')

#Step4:
# Create a Hand Class. In addition to holding card objects dealt from the Deck, the Hand Class
# may be used to calculate the value of those cards using the values dictionary defined above
# It may also need to adjust the value of Aces when appropriate


class Hand():

    def __init__(self):
        self.cards = [] #start with an empty list as we did in the Deck class
        self.value = 0 #start with zero value
        self.aces = 0 #add an attribute to keep track of aces

    def add_card(self,card):
        #card passed in will be the single_card we grabbed from deal function of Deck Class
        #Deck.deal() --> Single card --> Card(suit,rank)
        self.cards.append(card)
        #This will return some number containing card's value
        #Adjusting the value to the card which is just added to the list
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        #Initially we consider Ace as 11
        #if total card values > 21 and we still have an Ace
        #then we reduce 10 from total value and consider Ace as 1
        #and we reduce the ace count by 1
        while self.value > 21 and self.aces > 0: #self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

new_deck4 = Deck()
new_deck4.shuffle()
#Deal 1 card from Deck card (suit,rank)
my_card = new_deck4.deal()
print('My Card: ',my_card)
#Player
test_player = Hand()
test_player.add_card(my_card)
print(test_player.cards[0])
print(test_player.value)

print('***************CHIPS*********************')

#Step5:
# Create a Chips Class. In addition to deck of cards and hands, we need to keep track of
# player's starting chips, bets and ongoing winnings. This could be done using global variables
# but we will make a Chips Class instead.

class Chips():

    def __init__(self,total=100):
        self.total = total #This can be set to default or a value supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

print('***************FUNCTION FOR TAKING BET*********************')
#Step6:
# Write a function for taking bet
# Since we are asking user for an input value, this would be a good place to use try/except
# Remember to check that a player's bet can be covered by their available chips

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have {}'.format(chips.total))
            else:
                break


print('***************FUNCTION FOR TAKING HITS*********************')
#Step7:
# Write a function for taking hits
# Either player can take hits until they bust. This function will be called in Gameplay
# anytime a player requests a hit or a dealer's hand is less than 17. It should take in
# Deck and Hand objects as arguments, and deal one card off the Deck and add it to the Hand
# You may want to check for Aces in the event that a player's hand exceeds 21

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

print('***************FUNCTION FOR PROMPTING THE PLAYER TO HIT OR STAND*********************')
#Step8:
# Write a function for prompting the player to hit or stand
# This function should accept Deck and player's Hand as arguments, and assign playing as
# global variable. If the Player Hits, employ the hit() function above. If the Player Stands,
# set the playing variable to False - this will control the behavior of a while loop later
# on in our code.

def hit_or_stand(deck,hand):
    global playing #to control an upcoming while loop
    while True:
        x = input('Hit or Stand? Enter H or S : ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I didn't understand that, Please enter H or S only!")
            continue

        break

print('***************FUNCTION TO DISPLAY CARDS*********************')

def show_some(player,dealer):

    print('DEALERS HAND:')
    print('*****************************')
    print('One Card Hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    print('*****************************')
    for card in player.cards:
        print(card)
    print('\n')

def show_all(player,dealer):

    print('DEALERS HAND:')
    print('*****************************')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    print('*****************************')
    for card in player.cards:
        print(card)
    print('\n')


#Step9:
# Write a function to display cards. When the game starts, and each time player takes a card,
# the dealer's first card is hidden and all of player's cards are visible. At the end of the
# hand, all cards are shown, and you may want to show each hand's total value. Write a
# function for each of these scenarios


print('***************FUNCTION TO HANDLE END OF GAME SCENARIOS*********************')
#Step9:
# Write a function to handle end of game scenarios.
# Remember to add player's hand, dealer's hand and chips as needed

def player_busts(player,dealer,chips):
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()

#If both player and dealer got 21
def push(player,dealer):
    print('Dealer and Player tie! PUSH')

print('***************GAME LOGIC*********************')

while True:

    #Print an opening statement
    print('WELCOME OF BLACKJACK')

    #Create and shuffle the deck, deal 2 cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Setup the Player's chips
    player_chips = Chips()

    #Prompt the player for their bet
    take_bet(player_chips)

    #Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing: #recall this variable from our hit or stand function

        #Prompt for player to Hit or Stand
        hit_or_stand(deck,player_hand)

        #Show cards(but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        #If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    #If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value < 21:
        while dealer_hand.value < player_hand.value: #while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        #Show all cards
        show_all(player_hand,dealer_hand)

        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    #Inform player of their remaining chips total
    print("\n Player's total chips are at: {} ".format(player_chips.total))

    #Ask to play again
    new_game = input("Would you like to play another hand? Y or N : ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break



#CARD class has 3 properties - SUITE RANK VALUE
#Should be able to understand Suite of the card - Heart/Diamond/Spades/Club
#Should be able to understand Rank of the card - 2-10/Jack/Queen/King/Ace
#Should be able to understand integer value corresponding Rank of the card

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
          'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#Create a dictionary for Card rank and their values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    #To print actual card
    def __str__(self):
        return self.rank + " of " + self.suit

two_of_hearts = Card('Hearts','Two')
three_of_clubs = Card('Clubs','Three')
print('*************CARD OBJECT AND ITS ATTRIBUTES***********************')
print(two_of_hearts)
print('Suit: ',two_of_hearts.suit)
print('Rank: ',two_of_hearts.rank)
print('Value: ',two_of_hearts.value)
#print(values[two_of_hearts.rank])

print('*************CARD OBJECT AND ITS ATTRIBUTES***********************')

print(three_of_clubs)
print('Suit: ',three_of_clubs.suit)
print('Rank: ',three_of_clubs.rank)
print('Value: ',three_of_clubs.value)

print('**************CARDS COMPARISON**********************')

#Card value comparison
print(two_of_hearts.value < three_of_clubs.value)

class Deck:

    def __init__(self):
        #Create a deck that contains all 52 card objects
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    #Get one card from the list of cards
    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
print(new_deck.all_cards) #Prints card objects

print('************FIRST CARD IN THE DECK************************')

first_card = new_deck.all_cards[0]
print(first_card) #Prints first card object in the list as per format defined in __str__ method

print('*************BOTTOM CARD IN THE DECK***********************')

bottom_card = new_deck.all_cards[-1]
print(bottom_card) #Prints last card object in the list as per format defined in __str__ method

print('************LIST OF ALL CARDS IN DECK************************')
#Prints all 52 card objects e.g. Two of Hearts, Ace of Clubs, Seven of Spades, King of Diamonds
for card_object in new_deck.all_cards:
    print(card_object)

print('*************CARDS SHUFFLED***********************')

#Shuffling the cards and checking which one is the top and bottom card
new_deck1 = Deck()
new_deck1.shuffle()
print('Top Card: ',new_deck1.all_cards[0])
print('Bottom Card: ',new_deck1.all_cards[-1])

print('***************GRAB A CARD FROM SHUFFLED DECK*********************')
#Shuffling the cards and grab one from the deck of cards
new_deck2 = Deck()
new_deck2.shuffle()
my_card = new_deck2.deal_one()
print('My Card: ',my_card)

print('***************PLAYER*********************')

class Player:

    def __init__(self,name):
        self.name = name
        #Each player should have an empty hand
        self.all_cards = []

    #Add/Remove cards to get a player's current hand
    def remove_one(self):
        # When a player plays a single card, we grab card from top of the card list - means from index 0 of card list
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):

        # When a player adds multiple cards(list), we add to bottom of the card list - means extend cards to the card list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # When a player adds a card, we add to bottom of the card list - means append card to the card list
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

new_player = Player('Sandeep')
print(new_player)
print('****************************************')
new_player.add_cards(my_card)
print(new_player)
print('***************PRINT PLAYERS CARD/HAND*************************')
print(new_player.all_cards[0])
print('***************ADD MULTIPLE CARDS*************************')
new_player.add_cards([my_card,my_card,my_card,my_card])
print(new_player)
print('***************REMOVE CARDS*************************')
new_player.remove_one()
print(new_player)

print('***************GAME SETUP*************************')
player_one= Player('One')
player_two= Player('Two')

new_Deck = Deck()
new_Deck.shuffle()

#Split cards between 2 players
for x in range(26):
    player_one.add_cards(new_Deck.deal_one())
    player_two.add_cards(new_Deck.deal_one())

print('Player1 Cards Count:',len(player_one.all_cards))
print('Player1 First Card:',player_one.all_cards[0])
print('Player2 Cards Count:',len(player_two.all_cards))
print('Player2 First Card:',player_two.all_cards[0])

game_on = True

#while GameOn
round_num = 0 #Number of rounds the game goes on
while game_on:
    round_num += 1
    print(f'Round {round_num}:')

    if len(player_one.all_cards) ==0:
        print('Player One, out of cards! PLAYER TWO WINS!')
        game_on = False
        break
    if len(player_two.all_cards) ==0:
        print('Player Two, out of cards! PLAYER ONE WINS!')
        game_on = False
        break

    #START A NEW ROUND
    #Current cards in play for player one
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    # Current cards in play for player one
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #Cards Comparison
    #3 Situations - Player1 > Player2  Player2 > Player1  Player1 == Player2

    #Assuming we are at war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war! Game Over at War')
                print('PLAYER TWO WINS!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war! Game Over at War')
                print('PLAYER ONE WINS!')
                game_on = False
                break

            #Adding 5 more cards for each player to play WAR
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())




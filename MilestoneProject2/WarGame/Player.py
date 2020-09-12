#PLAYER CARD: Who can hold card from a deck

#Player card will be used to hold a player's current list of cards
#A player should be able to add or remove cards from their hand(list of card objects)
# Translate a Deck/Hand of cards with a top and bottom to a Python list

# Card is typically drawn from the top of the deck
# Card is typically drawn to bottom of the deck

#Player class will have a self.all_cards list

cards = ['A','B','C']
#When a player plays a single card, we grab card from top of the card list - means from index 0 of card list
cards.pop(0)

#When a player adds a card, we add to bottom of the card list - means append card to the card list
cards.append('W')

#When a player adds multiple cards(list), we add to bottom of the card list - means extend cards to the card list
new = ['X','Z']
cards.extend(new)  #Extend takes a list and merges with existing list
#Don't use append() as list becomes nested
#e.g. cards.append(new) --> ['B','C',['X','Z']]

#class Player:
from . import card
from random import randint

class Deck:
    def __init__( self ):
        self.cards = []
        self.add_card()

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    
    def deal(self):
        card_position = randint(0,len(self.cards)-1)
        card = self.cards[card_position]
        self.cards.pop(card_position)
        return card

    # @property
    def card_count(self):
        return len(self.cards)

    def add_card(self):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )
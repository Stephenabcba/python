class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 100
        self.stayed = False
        self.busted = False
        self.blackjack = False
        self.has_five_cards = False

    def clear_hand(self):
        self.hand.clear()

    def clean_up(self):
        self.busted = False
        self.stayed = False
        self.blackjack = False
        self.has_five_cards = False
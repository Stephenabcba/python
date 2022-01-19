from classes.deck import Deck
from classes.card import Card
from classes.player  import Player

game_actions = ("hit", "stay")

class game_manager: #the dealer
    #so what does the game manager need to do
    #Deal a card to the player
    #compare values against the rules
    #Give the player choices they can make
    #payout the player if they win
    #collect if the player loses
    #clear out a player's hand
    def __init__(self, name):
        self.player = Player(name)
        self.house = Player("House")
        self.deck = Deck()


        #Debug to show initial dealing
        # print("===== Initial Dealing =====")
        # print("----- Player hand -----")
        # for card in self.player.hand:
        #     card.card_info()
        # print("----- House hand -----")
        # for card in self.house.hand:
        #     card.card_info()
        # print("===== Initial Deal End =====")
    def hit_or_stay(self):
        if self.check_bust(self.player):
            self.player.busted = True
            return self

        if self.check_five_cards(self.player):
            self.player.stayed = True
            self.player.has_five_cards = True
            return self
        input_validity = False
        while (not input_validity):
            choice = input(f"Your hand is worth {hand_value(self.player.hand)}. Would you like to hit or stay?\n").lower()
            input_validity = self.validate_input(choice, game_actions)
        if (choice == "hit"):
            self.hit(self.player)
        if (choice == "stay"):
            self.stay(self.player)
        # if (choice == "fold"):
        #     self.fold(self.player)
        return self #figure out what should be returned... until then chaining
    
    def house_hit_or_stay(self):
        if self.player.busted:
            return self
        if self.player.has_five_cards:
            return self
        if self.player.blackjack:
            return self
        while (hand_value(self.house.hand) < 16):
            self.hit(self.house)
        if self.check_bust(self.house):
            self.house.busted = True
        return self

    def hit(self, target): #it's deal card
        if(target.stayed == False):
            target.hand.append(self.deck.deal())
        
    def stay(self, player):
        player.stayed = True
        return self
    
    # def fold(self, player):
    #     pass
    
    def compare(self):
        player_hand = hand_value(self.player.hand)
        house_hand = hand_value(self.house.hand)
        print(f"PLAYER HAND IS {player_hand}\nHOUSE HAND IS {house_hand}")
        if (self.player.busted):
            print(f"Player has busted with a {hand_value(self.player.hand)}")
            print("House wins!")
            return False
        elif self.player.has_five_cards:
            print(f"Player has 5 cards!")
            print("Player wins!")
            return True
        elif self.house.busted :
            print(f"House has busted with a {hand_value(self.house.hand)}")
            print("Player wins!")
            return True
        elif(player_hand > house_hand):
            print("Player wins!")
            return True
        else:
            print("House wins!")
            return False
    
    def validate_input(self, choice, li):
        return choice in li

    def check_bust(self, player):
        if hand_value(player.hand) > 21:
            # print(f"Your hand is {hand_value(player.hand)}. You have busted!")
            return True
        return False
    
    def check_wager(self,player):
        valid_wager = False
        while not valid_wager:
            amount =  input(f"How many points are you going to wager?\nAvailable Points: {player.points}\n")
            valid_wager = (int(amount) >= 0 and int(amount) <= player.points)
            if not valid_wager : 
                print("Invalid Wager!\nHas to be Greater than 0 and less than available points")
        return int(amount)

    def mod_points(self, amount):
        self.player.points += amount

    def reset_stay_bust(self):
        self.player.clean_up()
        self.house.clean_up()
        return self

    def check_card_remain(self):
        print(f"There are {self.deck.card_count()} cards in the deck")
        if self.deck.card_count() < 15:
            self.deck.add_card()
        # self.deck.show_cards()
            print(f"Adding Another Deck of Cards\nNow At {self.deck.card_count()} Cards")
        return self
    
    def starting_deal(self):
        for i in range(2):
            self.hit(self.house)    
            self.hit(self.player)

    def clear_hands(self):
        self.player.clear_hand()
        self.house.clear_hand()

    def check_black_jack(self, target):
        if len(target.hand) == 2 and hand_value(target.hand) == 21:
            target.stayed = True
            target.blackjack = True
            print(f"{target.name} got BLACKJACK 21!")
            return True
        return False

    def force_blackjack(self,target):
        target.clear_hand()
        target.hand.append(Card("Spade",1,"Ace"))
        target.hand.append(Card("Spade",13,"King"))

    def check_five_cards(self,target):
        if len(target.hand) >= 5:
            return True
        return False

    def force_five_cards(self,target):
        target.clear_hand()
        target.hand.append(Card("Spade",1,"Ace"))
        target.hand.append(Card("Spade",1,"Ace"))
        target.hand.append(Card("Spade",1,"Ace"))
        target.hand.append(Card("Spade",1,"Ace"))
        target.hand.append(Card("Spade",1,"Ace"))

def hand_value(hand):
    total = 0
    has_ace = False
    for card in hand:
        if (card.point_val >= 10):
            total += 10
        elif (card.point_val == 1):
            if (total + 11 > 21):
                total += 1
            else:
                total += 11
                has_ace = True
        else:
            total += card.point_val
        if (total > 21 and has_ace): # checks if an ace valued at 11 exists when the total exceeds 21
            total -= 10
            has_ace = False
    return total
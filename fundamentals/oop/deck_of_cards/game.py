from classes.deck import Deck
from classes.player import Player
from classes.game_manager import game_manager
# import random
#Making Blackjack
bicycle = Deck()

# bicycle.show_cards()


#"split","double down",



GM = game_manager(input("What's your name?\n"))

game_running = True

while(game_running):
    print("*" * 80)
    wager = GM.check_wager(GM.player)
    GM.check_card_remain()
    GM.starting_deal()
    # Testing Code Uncomment to test certain things
    # GM.force_blackjack(GM.player)
    # GM.force_blackjack(GM.house)
    # GM.force_five_cards(GM.player)
    GM.check_black_jack(GM.player)
    GM.check_black_jack(GM.house)
    while (not GM.player.stayed and not GM.player.busted and not GM.house.blackjack):
        GM.hit_or_stay()
    player_wins = GM.house_hit_or_stay().compare()
    if not player_wins:
        wager = wager * -1
    GM.mod_points(wager)
    GM.clear_hands()
    if GM.player.points > 0 :   
        valid_choice = False
        while not valid_choice:
            choice = input("Play Again?\nyes   no\n").lower()
            if choice == "yes":
                valid_choice = True
                GM.reset_stay_bust()
            elif choice == "no":
                valid_choice = True
                game_running = False
    else:
        game_running = False


points = GM.player.points
if(points <= 0):
    print("You lost a lot of money")
elif(points <= 100):
    print("You left with less than what you started")
else:
    print(f"Congrats! you left with {points} Points!")
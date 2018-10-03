# import player
from player import *
from deck import *

'''
one player vs automated dealer
player can hit or stand
player must be able to pick betting amount
keep track of players money
alert player to wins, busts, or losses
'''


class BlackJack:

    def __init__(self):
        # self.player = Player()
        self.deck = Deck()
        self.dealer_hand = ""

    def draw_cards(self, num_cards):
        cards = []
        for _num in range(0, num_cards):
            cards.append(self.deck.card_deck.pop(0))

        return cards

    def show_hands(self):
        # need to handle when to show dealers other cards
        print(
            f"player's hands: [{self.player.hand[0][0]}] [{self.player.hand[1][0]}]")
        print(f"dealer's hands: [{self.dealer_hand[0][0]}] [?]")

    def deal(self, min_cards=4):
        '''
        While loop will run until the player quits or runs out of money
        The players is dealt two hands. The dealer shows one card and 
        the other is face down
        '''
        keep_playing = True
        print(len(self.deck.card_deck))

        while keep_playing:
            if len(self.deck.card_deck) <= min_cards:
                keep_playing = False
            self.deck.shuffle_deck()
            self.player.hand = self.draw_cards(2)
            self.dealer_hand = self.draw_cards(2)
            self.show_hands()
            print(len(self.deck.card_deck))
            keep_playing = False

    def initialize_game(self):
        while True:
            try:
                starting_amount = float(input("Enter starting bet:  "))
                if starting_amount < 0:
                    raise ValueError
            except:
                print("Amount must be a positive number")
            else:
                break

        self.player = Player(starting_amount)
        self.deal()


if __name__ == '__main__':
    blackjack = BlackJack()
    blackjack.initialize_game()
    print(blackjack.player.total)

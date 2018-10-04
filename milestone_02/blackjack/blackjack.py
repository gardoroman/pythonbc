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

    def check_cards(self, cards):
        card_count = 0
        for card in cards:
            card_count += card[1]
        return card_count

    def prompt_player(self):
        keep_hitting = True
        print(f'\n\nplayer hand is {self.player.hand}')
        while keep_hitting:
            choice = input("type 'h' for hit or 's' for stand:  ")
            if choice == 'h':
                self.player.hand += self.draw_cards(1)
                # draw cards
                # add points
                card_count = self.check_cards(self.player.hand)
                self.format_hands(self.player.hand)
                print(f'current total: {card_count}')
            else:
                print("It is now the dealers turn")
                keep_hitting = False

    def format_hands(self, cards):
        card_string = ' '
        for card in cards:
            card_string += '[' + card[0] + '] '
        print(card_string)

    def show_hands(self, hide_card=False):
        # need to handle when to show dealers other cards
        # print(
        #     f"player's hands: [{self.player.hand[0][0]}] [{self.player.hand[1][0]}]")
        # print(f"dealer's hands: [{self.dealer_hand[0][0]}] [?]")

        self.format_hands(self.player.hand)
        if hide_card:
            print(f' [{self.dealer_hand[0][0]}] [?]')
        else:
            self.format_hands(self.dealer_hand)

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
            self.show_hands(True)
            self.prompt_player()
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

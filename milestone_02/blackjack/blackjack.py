
from player import *
from deck import *

# import player
# import deck


class BlackJack:
    '''
    one player vs automated dealer
    player can hit or stand
    player must be able to pick betting amount
    keep track of players money
    alert player to wins, busts, or losses
    '''

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
        # print(f'\n\nplayer hand is {self.format_hands(self.player.hand)}')
        is_game_over = False
        while keep_hitting:
            choice = input("\ntype 'h' for hit or 's' for stand:  ")
            if choice == 'h':
                self.player.hand += self.draw_cards(1)
                # draw cards
                # add points
                self.player.score = self.check_cards(self.player.hand)
                print(f'total points: {self.player.score}')
                self.format_hands(self.player.hand)
                if self.player.score > 20:
                    is_game_over = True
                    keep_hitting = False
                    if self.player.score > 21:
                        result = self.bet_amount * -1
                    elif self.player.score == 21:
                        result = self.bet_amount

                    self.player.update_info(result)

            else:
                print("It is now the dealers turn")
                keep_hitting = False

        return is_game_over

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
            self.bet_amount = self.get_amount("How much will you bet?  ")
            self.player.bet(self.bet_amount)
            self.deck.shuffle_deck()
            self.player.hand = self.draw_cards(2)
            self.dealer_hand = self.draw_cards(2)
            self.show_hands(True)
            is_game_over = self.prompt_player()
            if not is_game_over:
                self.automate_dealer()
            print(len(self.deck.card_deck))
            keep_playing = False

    def automate_dealer(self):
        print("The dealer plays")
        keep_hitting = True
        while keep_hitting:
            self.format_hands(self.dealer_hand)
            dealer_score = self.check_cards(self.dealer_hand)
            if dealer_score > 20:
                keep_hitting = False
                if dealer_score > 21:
                    result = self.bet_amount
                    print("You win")
                elif dealer_score == 21:
                    # self.player.wins += 1
                    print("Dealer wins")
                    keep_hitting = False
                    result = self.bet_amount * -1
                self.player.update_info(result)
            self.dealer_hand += self.draw_cards(1)

    def get_amount(self, msg):
        while True:
            try:
                total_amount = float(input(msg))
                if total_amount < 0:
                    raise ValueError
            except:
                print("Amount must be a positive number")
            else:
                break
        return total_amount

    def initialize_game(self):
        total_amount = self.get_amount("How much do you have to bet?  ")
        self.player = Player(total_amount)
        self.deal()
        print(self.player.total)


if __name__ == '__main__':
    blackjack = BlackJack()
    blackjack.initialize_game()

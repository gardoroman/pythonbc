
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
        self.ace = ['A', 11]

    def draw_cards(self, num_cards):
        cards = []
        for _num in range(0, num_cards):
            cards.append(self.deck.card_deck.pop(0))

        return cards

    def get_score(self, cards):
        card_count = 0
        for card in cards:
            card_count += card[1]
        return card_count

    def convert_to_one(self, cards, num_aces):
        '''
        Iterate through hands and covert specified
        number of aces to one if it is not the dealer.
        If it is the dealer's hand only convert one at a time.
        '''
        pos = 0
        for _num in range(0, num_aces):
            ace_index = cards.index(self.ace, pos)
            cards[ace_index][1] = 1
            pos += 1
        


    def handle_aces(self, cards, is_player=False):
        if is_player:
            aces = cards.count(self.ace)
            if aces > 0:
                msg = f'{str(aces)} Aces. How many do you want to switch? '
                switched_aces = int(self.get_amount(msg))
                if switched_aces > 0:
                    self.convert_to_one(cards, switched_aces)
        else:
            self.convert_to_one(cards, 1)

    # def check_player_points(self, cards):


    def prompt_player(self):
        keep_hitting = True
        # print(f'\n\nplayer hand is {self.format_hands(self.player.hand)}')
        is_game_over = False
        while keep_hitting:
            self.handle_aces(self.player.hand, True)
            # choice = input("\ntype 'h' for hit or 's' for stand:  ")
            # if choice == 'h':
            #     self.player.hand += self.draw_cards(1)
                # draw cards
                # add points
            self.player.score = self.get_score(self.player.hand)
            #  = self.handle_aces(self.player.hand)
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

                break
            
            
            choice = input("\ntype 'h' for hit or 's' for stand:  ")
            if choice == 'h':
                self.player.hand += self.draw_cards(1)

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
                print("out of cards")
                keep_playing = False
            
            self.bet_amount = self.get_amount("How much will you bet?  ")
            self.player.bet(self.bet_amount)
            # self.deck.shuffle_deck()
            self.player.hand = self.draw_cards(2)
            self.dealer_hand = self.draw_cards(2)
            # self.player.hand = [['A', 11], ['K', 10]]
            # self.dealer_hand = [['A', 11], ['K', 10]]
            self.show_hands(True)
            is_game_over = self.prompt_player()
            print(f'gameover {is_game_over}')
            if not is_game_over:
                return self.automate_dealer()
            
            print(len(self.deck.card_deck))
            keep_playing = False


        

    def automate_dealer(self, min_cards=4):

        print("The dealer plays")
        keep_hitting = True
        player_score = self.player.score
        # player_score = 15
        # self.dealer_hand = [['4', 4], ['7', 7], ['A', 11]]

        while keep_hitting:
            if len(self.deck.card_deck) <= min_cards:
                print("out of cards")
                keep_hitting = False
            aces = self.dealer_hand.count(self.ace)
            self.format_hands(self.dealer_hand)
            dealer_score = self.get_score(self.dealer_hand)
            print(f"dealer score {dealer_score}")
            

            if dealer_score < 17:
                self.dealer_hand += self.draw_cards(1)
            elif dealer_score < player_score:
                result = self.bet_amount
                keep_hitting = False             
            elif player_score < dealer_score < 22:
                result = self.bet_amount * -1
                keep_hitting = False
            elif dealer_score > 21 and aces == 0:
                result = self.bet_amount
                keep_hitting = False             
            elif dealer_score > 21 and aces > 0:
                self.handle_aces(self.dealer_hand)
            elif 16 < dealer_score == player_score:
                result = 0
                keep_hitting = False


            if not keep_hitting:
                self.player.update_info(result)
                return False
                

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
        '''
        Create while loop to continue game
        get the result form first game and give option to continue
        '''
        keep_playing = True
        while keep_playing:
            total_amount = self.get_amount("How much do you have to bet?  ")
            self.deck.shuffle_deck()
            self.player = Player(total_amount)
            keep_playing = self.deal()
            if not keep_playing:
                msg = "Keep playing 'y' or 'n'"
                player_response = input(msg)
                if player_response == 'y':
                    keep_playing = True
                else:
                    print('Game Over')
                    print(self.player.total)


if __name__ == '__main__':
    blackjack = BlackJack()
    blackjack.initialize_game()

# import player
from player import *
# import deck


# class Player:

#     def __init__(self, total):
#         self.total = total

#     def bet(self, amount):
#         updated_total = self.total - amount
#         if updated_total < 0:
#             print(f'Max bet size is {self.total}')
#         else:
#             self.total = updated_total

#     def add_winnings(self, winnings):
#         self.total += winnings
#         print(f'Total balance is now {self.total}')


class BlackJack:

    # def __init__(self, player, deck):
    #     self.player = Player()
    #     self.deck = Deck()

    def play(self):
        '''
        While loop will run until the player quits or runs out of money
        '''

    def initialize_game(self):
        while True:
            try:
                starting_amount = float(input("Enter starting amount:  "))
                if starting_amount < 0:
                    raise ValueError
            except:
                print("Amount must be a positive number")
            else:
                break

        self.player = Player(starting_amount)


if __name__ == '__main__':
    blackjack = BlackJack()
    blackjack.initialize_game()

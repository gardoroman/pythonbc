class Player:

    def __init__(self, total):
        self.total = total
        # print(f'total is {total}')

    def bet(self, amount):
        updated_total = self.total - amount
        if updated_total < 0:
            print(f'Max bet size is {self.total}')
        else:
            self.total = updated_total

    def add_winnings(self, winnings):
        self.total += winnings
        print(f'Total balance is now {self.total}')

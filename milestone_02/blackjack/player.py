class Player:

    def __init__(self, total):
        self.total = total
        self.wins = 0
        self.losses = 0
        self.draws = 0
        # print(f'total is {total}')

    def bet(self, amount):
        # updated_total = self.total - amount

        while amount < 0:
            print(f'Max bet size is {self.total}')

            amount = float(input("Enter a new bet "))
            # updated_total = self.total - amount

        # self.total = updated_total

    def update_info(self, bet_amount):
        if bet_amount < 0:
            self.losses += 1
        elif bet_amount == 0:
            self.draws += 1
        else:
            self.wins += 1

        self.total += bet_amount
        if self.total == 0:
            print("Game Over")
        print(f'Total balance is now {self.total}')
        print(f'Wins: {self.wins}')
        print(f'Losses: {self.losses}')
        print(f'Draws: {self.draws}')

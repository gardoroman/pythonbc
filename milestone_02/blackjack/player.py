class Player:

    def __init__(self, total):
        self.total = total
        self.wins = 0
        self.losses = 0
        self.draws = 0
        # print(f'total is {total}')

    def bet(self, amount):
        updated_total = self.total - amount
        if updated_total < 0:
            print(f'Max bet size is {self.total}')
        else:
            self.total = updated_total

    def update_info(self, result):
        if result < 0:
            self.losses += 1
        elif result == 0:
            self.draws += 1
        else:
            self.wins += 1

        self.total += result
        if self.total == 0:
            print("Game Over")
        print(f'Total balance is now {self.total}')
        print(f'Wins: {self.wins}')
        print(f'Losses: {self.losses}')
        print(f'Draws: {self.draws}')

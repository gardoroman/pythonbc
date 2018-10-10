from random import shuffle


class Deck:

    cards = [
        ['2', 2],  ['3', 3],  ['4', 4],
        ['5', 5],  ['6', 6],  ['7', 7],
        ['8', 8],  ['9', 9],  ['10', 10],
        ['J', 10], ['Q', 10], ['K', 10],
        ['A', 11]
    ]
    # cards = [
    #     ['A', 11],  ['A', 11],  ['A', 11],
    #     ['A', 11],  ['A', 11],  ['A', 11],
    #     ['A', 11],  ['9', 9],  ['10', 10],
    #     ['J', 10], ['Q', 10], ['K', 10],
    #     ['A', 11]
    # ]

    def __init__(self):
        print
        self.shuffle_deck()

    def shuffle_deck(self):
        '''
        adds 4 suits to the deck
        '''
        self.card_deck = Deck.cards * 4
        # use random.rand_int(first number inclusive, second number inclusive)
        shuffle(self.card_deck)


if __name__ == '__main__':
    deck = Deck()
    print(deck.card_deck)

ttt = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def print_board():
    board = ''
    # for row in ttt:
    #     print_row = ['[' + i + ']' for i in row]
    #     board += ''.join(print_row) + '\n'

    for i in range(0, 3):
        row = ttt[i * 3:(i + 1) * 3]
        print_row = ['[' + str(i) + ']' for i in row]
        board += ''.join(print_row) + '\n'

    return board


def check_sub_array(sub_array, token):
    return {token} == set(sub_array)


def is_sub_array_valid()


def directional_search(row, col):
    '''
    parameter based search
    horizontal, if position 
    '''


def check_for_winner(token):
    '''
    get subset of three and run set() 
    to see if the set only has a length
    of 1 and is equal to that token
    '''

    for position in ttt:
        '''
        loop through each index,
        and generate a sub_array for
        horizontal, vertical, and diagonal
        if valid sub_array check if it's valid
        '''


def get_input(player, token):
    player_input = input(
        player + f" player {player} please select position number or 'q' to quit: ")
    ttt[int(player_input)] = token

    print_board()
    check_for_winner(token)
    return 'q'


is_unfinished = True

while is_unfinished:
    player_one = get_input("one", 'x')
    player_one = get_input("two", 'o')

    # ttt[int(row), int(col)] = 'x'
    # print(ttt[0][0])
    print(print_board())
    if player_one == 'q':
        is_unfinished = False

ttt = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board():
    board = ''

    for i in range(0, 3):
        row = ttt[i * 3:(i + 1) * 3]
        print_row = ['[' + str(i) + ']' for i in row]
        board += ''.join(print_row) + '\n'

    return board


def check_sub_list(sub_list, token):
    # print("check sub list")
    for i in sub_list:
        if i != token:
            return False
    return True


def is_sub_list_valid(position, token):
    '''
    check position for all its rows
    if any row is a winning row,
    return true
    '''
    (pos_quotient, pos_remainder) = divmod(position, 3)
    if pos_remainder == 0:
        horizontal_list = ttt[position: position + 3:]
        horizontal_check = check_sub_list(horizontal_list, token)
        if horizontal_check:
            return True

    if pos_quotient == 0:
        vertical_list = ttt[position::3]
        vertical_check = check_sub_list(vertical_list, token)
        if vertical_check:
            return True
        if position == 0:
            diagonal_lr_list = ttt[0::4]
            diagonal_lr_check = check_sub_list(diagonal_lr_list, token)
            if diagonal_lr_check:
                return True
        if position == 2:
            diagonal_rl_list = ttt[-3:1:-2]
            print(f"list is {diagonal_rl_list}")
            diagonal_rl_check = check_sub_list(diagonal_rl_list, token)
            if diagonal_rl_check:
                return True
        return False


def check_for_winner(token):
    '''
    get subset of three and run set()
    to see if the set only has a length
    of 1 and is equal to that token
    '''
    positions = [i for i, item in enumerate(ttt) if item == token]

    if len(positions) < 3:
        return False

    for position in positions:
        '''
        loop through each index,
        and generate a sub_list for
        horizontal, vertical, and diagonal
        if valid sub_list check if it's valid
        '''
        result = is_sub_list_valid(int(position), token)
        if result:
            return True


def get_input(player):
    '''
    Receives token of the current player.
    Calls functions to 
    '''
    valid_move = False
    while not valid_move:
        player_input = input(
            f" player {player} please select an empty position or press 'q' to quit: ")

        if player_input == 'q':
            return 'q'
        elif ttt[int(player_input)] == ' ':
            ttt[int(player_input)] = player
            valid_move = True

    print_board()
    return check_for_winner(player)


current_player = "x"

finished = False

while not finished:
    play = get_input(current_player)
    print(print_board())
    if play == 'q':
        finished = True
    elif play == True:
        if play == True:
            print(f'player {current_player} wins!')
        finished = True
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"

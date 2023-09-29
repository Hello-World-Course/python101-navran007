name = input('Hello, whats your name?')
if len(name) > 1:
    board_size_as_str = input(f'{name}, please choose board size:')
    board_size = int(board_size_as_str)
    if 0 < board_size < 26:
        number_of_mines_as_str = input(f'{name}, for board size {board_size}, choose number of mines to allocate:')
        number_of_mines = int(number_of_mines_as_str)
        if 0 < number_of_mines < board_size // 2:
            print(f'player_name: {name}, board_size: {board_size}, num_of_mines: {number_of_mines}')
        else:
            print(f'{name} you entered illegal number of mines')
            number_of_mines = None
    else:
        print(f'{name} you entered illegal board size')
        board_size = None
else:
    print('Your name is too short')
    name = None

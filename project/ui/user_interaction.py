def is_name_valid(name):
    return len(name) > 1


def is_board_size_valid(board_size):
    return 0 < board_size < 26


def is_number_of_mines_valid(board_size, number_of_mines):
    return 0 < number_of_mines <= (board_size ** 2) // 2


def register_user():
    name = input('Hello, whats your name?')
    if is_name_valid(name):
        board_size_as_str = input(f'{name}, please choose board size:')
        board_size = int(board_size_as_str)
        if is_board_size_valid(board_size):
            number_of_mines_as_str = input(f'{name}, for board size {board_size}, choose number of mines to allocate:')
            number_of_mines = int(number_of_mines_as_str)
            if is_number_of_mines_valid(board_size, number_of_mines):
                return name, board_size, number_of_mines
            else:
                print(f'{name}, you have entered illegal number of mines')
        else:
            print(f'{name}, you have entered illegal board size')
    else:
        print('Your name is too short')

    return None, None, None


# user_name, user_board_size, user_num_mines = register_user()
# print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")

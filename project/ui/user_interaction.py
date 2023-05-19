player_name = None
board_size = None
number_of_mines = None

temp_name = input("Hello, whats your name?")
if len(temp_name) > 1:
    player_name = temp_name
    temp_board_size = int(input(f"{player_name}, please choose board size:"))
    if 0 < temp_board_size < 64:
        board_size = temp_board_size
        temp_number_of_mines = int(input(f"{player_name}, for board size {board_size}, choose number of mines to allocate:"))
        if 0 < temp_number_of_mines < 0.5 * board_size * board_size:
            number_of_mines = temp_number_of_mines
        else:
            print(f"{player_name}, you entered illegal number of mines")
    else:
        print(f"{player_name}, you entered illegal board size")
else:
    print("Your name is too short")

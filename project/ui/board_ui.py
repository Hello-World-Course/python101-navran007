def parse_cmd(cmd):
    parsed_cmd = cmd.split(' ')
    return parsed_cmd[0], parsed_cmd[1:]


def draw_board(board):
    columns = ' ' * 3 + ' '.join([chr(65 + i) for i in range(len(board))]) + ' \n'
    table_as_str = columns
    for row_idx in range(len(board)):
        row = [f'{row_idx}' + ' ' if row_idx < 10 else f'{row_idx}']
        for col_idx in range(len(board)):
            row.append(board[row_idx][col_idx])
        line = '|'.join(row) + '|\n'
        table_as_str += line

    return table_as_str


def convert_coords(location):
    A_ASCII_VAL = 65
    sep_idx = 0
    for idx, c in enumerate(location):
        if not c.isnumeric():
            sep_idx = idx
    return int(location[:sep_idx]), ord(location[sep_idx:]) - A_ASCII_VAL

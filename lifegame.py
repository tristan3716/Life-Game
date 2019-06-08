import curses
import copy
from random import choice


def end_curse():
    curses.endwin()


def load(path="inputdata.txt"):
    from atexit import register
    register(end_curse)  # Set "curses.endwin()" to be executed at the end
    inputfile = open(path, 'r')
    data = inputfile.read()
    inputfile.close()
    return data


def set_board(data):
    game_cell = []
    for i in range(0, 8):
        game_cell.append(data[(i*9): ((i+1)*9 - 1)])

    cur_board = [[0 for col in range(8)] for row in range(8)]

    for i in range(0, len(game_cell)):
        for j in range(0, len(game_cell)):
            if game_cell[i][j] == 'X':
                cur_board[i][j] = 0
            else:
                cur_board[i][j] = 1
    return cur_board


def print_board(board):
    win1 = curses.newwin(8+2, 8+2, 0, 0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)  # blank cell
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)  # alive cell
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_YELLOW)  # alive cell
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_YELLOW)  # alive cell
    curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_CYAN)  # border

    win1.attron(curses.color_pair(7))
    win1.border('|', '|', '-', '-', '*', '*', '*', '*')
    char = [' ', '-', 'G', '#']

    for x in range(0, len(board)):
        for y in range(0, len(board)):
            n = get_neighbour_count(x, y, board)
            # case 0: dead
            if board[x][y] == 0:
                case = 0
            # case 1: alive and disappear in the next generation
            elif n <= 1 or n >= 4:
                case = 1
            # case 2 ~ 3: alive and no disappear in the next generation
            elif choice([True, False]):
                case = 2
            else:
                case = 3
            win1.attron(curses.color_pair(case+1))  # set attribute
            win1.addch(x+1, y+1, char[case])  # print character

    win1.refresh()
    stdscr.refresh()
    pass


def is_valid_position(pos, new_pos):
    (x, y) = (new_pos[0], new_pos[1])
    if pos == new_pos:  # invalid_self
        return False
    if x < 0 or x > 7 or y < 0 or y > 7:  # invalid_out_of_bound
        return False

    return True


def get_neighbour_count(x, y, board):
    cell = x, y
    neighbours = []
    # inspect the surrounding 9 spaces
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            pos = (x + j, y + i)
            if is_valid_position(cell, pos):
                neighbours.append(pos)

    number_of_living_neighbor = 0
    for neighbour in neighbours:
        (_x, _y) = neighbour
        if board[_x][_y] == 1:  # if neighbor is alive
            number_of_living_neighbor += 1

    return number_of_living_neighbor


def run_life_game(board):
    board_cp = copy.deepcopy(board)
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            number_of_living_neighbor = get_neighbour_count(x, y, board)

            if board[x][y] == 0 and number_of_living_neighbor == 3:
                board_cp[x][y] = 1
            elif board[x][y] == 1 and number_of_living_neighbor <= 1:
                board_cp[x][y] = 0
            elif board[x][y] == 1 and (2 <= number_of_living_neighbor <= 3):
                board_cp[x][y] = 1
            elif board[x][y] == 1 and number_of_living_neighbor >= 4:
                board_cp[x][y] = 0

    return board_cp


if __name__ == "__main__":
    stdscr = curses.initscr()

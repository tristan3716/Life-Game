import sys

import lifegame
import os
import curses

data = lifegame.load()
cur_board = lifegame.set_board(data)
time = 500
time_integration = 0
lifegame.stdscr = curses.initscr()
curses.curs_set(0)

while True:
    next_board = lifegame.run_life_game(cur_board)
    lifegame.print_board(next_board)
    cur_board = next_board

    curses.napms(time)
    time_integration += time
    if time_integration > 10000:
        break

curses.endwin()

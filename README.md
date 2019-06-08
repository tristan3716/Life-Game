# Life-Game
Conway's game of life implemented (python with curses)

![gif animation of game-of-life](/images/gol.gif)

main.py execution logic
```python
board = initialize_board("input")

while True:
    print_board(board)
    board = get_next_board(board)
    
    sleep(500)
    if elapsed_time > 10000:
        break
```

lifegame.py execution logic 
```python
def run_life_game(board):  # get_next_board
    for x:
        for y:
            add_all_near_valid_cell_to_list()
            count_living_cell_from_list()
            check_next_cell_status()

    return board
```
# Life-Game
Conway's game of life implemented (python with curses)  
It's just a assignment. main.py was given  

![gif animation of game-of-life](/images/gol.gif)

## Input
Default state of cells  
Filename: inputdata.txt  
Consists of O (Alive state cell) or X (Dead State cell)

e.g.
```
XXXXXOXO
XXXXXOOX
XXXXXXOX
XXXXXXXX
XXXXXXXX
XXXXXXXX
OOOXXXXX
XXXXXXXX
```

### Execute 
run main.py

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
def get_next_board(board):
    for x:
        for y:
            add_all_near_valid_cell_to_list()
            count_living_cell_from_list()
            check_next_cell_status()

    return board
```

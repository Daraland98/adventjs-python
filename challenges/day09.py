'''The elves are playing with a magical train 🚂 that carries gifts. This train moves on a board represented by an array of strings.

The train consists of an engine (@), followed by its carriages (o), and must collect magical fruits (*) which serve as fuel. The movement of the train follows these rules:

You will receive two parameters board and mov.

board is an array of strings that represents the board:

· @ is the train's engine.
· o are the train's carriages.
· * is a magical fruit.
· · are empty spaces.

mov is a string that indicates the next movement of the train from the train's head @:

· 'L': left
· 'R': right
· 'U': up
· 'D': down.

With this information, you must return a string:

· 'crash': If the train crashes into the edges of the board or itself.
· 'eat': If the train collects a magical fruit (*).
· 'none': If it moves without crashing or collecting any magical fruit.

Example:'''

from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    rows, cols = len(board), len(board[0])
    
    # Find the position of the train's head (@)
    for r in range(rows):
        if '@' in board[r]:
            head_x, head_y = r, board[r].index('@')
            break
    
    # Define movement directions
    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    dx, dy = moves[mov]
    new_x, new_y = head_x + dx, head_y + dy

    # Check if the new head position is out of bounds
    if not (0 <= new_x < rows and 0 <= new_y < cols):
        return 'crash'

    # Check the cell at the new head position
    new_cell = board[new_x][new_y]
    if new_cell == 'o':  # Crash into itself
        return 'crash'
    elif new_cell == '*':  # Collect a magical fruit
        return 'eat'
    
    return 'none'  # Move without any even

board = ['·····', '*····', '@····', 'o····', 'o····']

print(move_train(board, 'U'))
## ➞ 'eat'
## Because the train moves up and finds a magical fruit

print(move_train(board, 'D'))
## ➞ 'crash'
## The train moves down and the head crashes into itself

print(move_train(board, 'L'))
## ➞ 'crash'
## The train moves to the left and crashes into the wall

print(move_train(board, 'R'))
## ➞ 'none'
## The train moves to the right and there is empty space on the right
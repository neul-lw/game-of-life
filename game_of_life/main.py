"""     
        Improve the User Interface
        Add a quit mode 
        Change the rules of Life
        Langton's ant 
"""

from pprint import pprint as pp
from random import random
import time 
import os 

DEAD = " "
ALIVE = "#"
#ALIVE = u"\u2588" as unicode color 

def random_state(cols: int, rows: int, freq: float):
    arr = []
    for row in range(rows):
        col = []
        for j in range(cols):
            dead_or_alive = random()
            if dead_or_alive >= freq:
                cell_state = 1
            else:
                cell_state = 0
            col.append(cell_state)
        arr.append(col)
    return arr


def next_state(init_state: list, mode: str):
    new_state = []
    
    for x in range(0, len(init_state)):
        new_state_row = []
        for y in range(0, len(init_state[0])):
            current_cell_value= init_state[x][y]
            next_elements = adjacent_elements(init_state, x, y, mode)
            if current_cell_value == 0 and next_elements.count(1) == 3:
                new_state_row.append(1)
            elif current_cell_value == 1:
                if 0 <= next_elements.count(1) <= 1:
                    new_state_row.append(0)
                if 2 <= next_elements.count(1) <= 3:
                    new_state_row.append(1)
                if next_elements.count(1) > 3:
                    new_state_row.append(0)
            else:
                new_state_row.append(init_state[x][y])
        new_state.append(new_state_row)
    return new_state 


def langton_ant():
    pass


def is_valid_pos(x: int, y: int, col_length: int, row_length: int):
    if x < 0 or y < 0 or x > col_length - 1 or y > row_length - 1:
        return 0 
    return 1


def adjacent_elements(init_state: list, x: int, y: int, mode: str):
    col_length = len(init_state)
    row_length = len(init_state[0])

    adj_arr = [] 

    if is_valid_pos(x-1, y-1, col_length, row_length):
        adj_arr.append(init_state[x-1][y-1])
    if is_valid_pos(x-1, y, col_length, row_length):
        adj_arr.append(init_state[x-1][y])
    if is_valid_pos(x-2, y, col_length, row_length) and mode == "von":
        adj_arr.append(init_state[x-2][y])
    if is_valid_pos(x-1, y+1, col_length, row_length):
        adj_arr.append(init_state[x-1][y+1])
    if is_valid_pos(x, y-1, col_length, row_length):
        adj_arr.append(init_state[x][y-1])
    if is_valid_pos(x, y-2, col_length, row_length) and mode == "von":
        adj_arr.append(init_state[x][y-2])
    if is_valid_pos(x, y+1, col_length, row_length):
        adj_arr.append(init_state[x][y+1])
    if is_valid_pos(x, y+2, col_length, row_length) and mode == "von":
        adj_arr.append(init_state[x][y+2])
    if is_valid_pos(x+1, y-1, col_length, row_length):
        adj_arr.append(init_state[x+1][y-1])
    if is_valid_pos(x+1, y, col_length, row_length):
        adj_arr.append(init_state[x+1][y])
    if is_valid_pos(x+2, y, col_length, row_length) and mode == "von":
        adj_arr.append(init_state[x+2][y])
    if is_valid_pos(x+1, y+1, col_length, row_length):
        adj_arr.append(init_state[x+1][y+1])

    
    return adj_arr


def load_board_state(path: str):
    arr = []
    with open(path, 'r') as f:
        f = [line.replace("\n", "") for line in f.readlines()]
        for line in f:
            row = []
            for n in line:
                n = int(n)
                row.append(n)
            arr.append(row)
    return arr 


def save_board_state(board: list, path: str):
    arr = [] 
    with open(path, 'w') as f:
        for row in board:
            row_arr = []
            for i in row:
                i = str(i)
                row_arr.append(i)
            row_arr.append('\n')
            f.write("".join(row_arr))


def render(board_state):
    print("----------GAME OF LIFE----------")
    for row in board_state:
        arr = []
        for cell in row: 
            if cell == 1:
                arr.append(ALIVE)
            else:
                arr.append(DEAD)
        pp(arr)
        arr.clear()


def run_game(board: list, duration: int, mode: str, loop: str):
    render(board)
    ns = next_state(board, mode)
    time.sleep(duration)
    
    if loop == "infinite":
        while True:
            render(ns)
            time.sleep(duration)
            ns = next_state(ns, mode)
    elif loop == "finite":
        loop_time = int(input("How many times you want to change the board? (should be bigger than 0): "))
        for i in range(loop_time):
            render(ns)
            time.sleep(duration)
            ns = next_state(ns, mode)


if __name__=="__main__":
    file_number = os.listdir('/home/neul/Documents/CS/Python/Advance-Beginners/game_of_life/boards/personal/')
    save_path = f'/home/neul/Documents/CS/Python/Advance-Beginners/game_of_life/boards/personal/personal_{len(file_number)+1}.txt'
    board_path = '/home/neul/Documents/CS/Python/Advance-Beginners/game_of_life/boards/presets/toad.txt'
    print("Welcome the Game of Life!")
    load_mode = input("Do you wanna play the (r)andom mode or load from a (f)ile? (r or f): ")
    game_mode = input("Do you want to play the game of life as default or with von neumann version: (press enter or enter 'von') ")
    loop_time = input("Do you want to run game for infinite or finite time (infinite or finite): ")
    if load_mode.lower() == 'r':
        user_cols = int(input("How many columns do you want to have on the board?: "))
        user_rows = int(input("How many rows do you want to have on the board?: "))
        user_freq = float(input("What is the frequency for dead state? (between 0-1): "))
        user_speed = float(input("How fast do you want to the board move? (in seconds): "))

        a_random_state = random_state(user_cols, user_rows, user_freq)
        save_or_not = input("Do you want to save the random state to a file? (y or n): ")
        if save_or_not == "y":
            save_board_state(a_random_state, save_path)
        run_game(a_random_state, user_speed, game_mode, loop_time)
    elif mode.lower() == 'f':
        file_path  = input("Please specify the path: ") 
        if not os.path.exists(file_path):
            print("Path is invalid!")
        else:
            user_speed = float(input("How fast do you want to the board move? (in seconds): "))
            board_f = load_board_state(file_path)
            run_game(board_f, user_speed, game_mode, loop_time)


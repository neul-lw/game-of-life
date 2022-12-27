""" Game rules:
    Any limep cell with 0 or 1 live neighbors becomes dead, 
    
        because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, 
        because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, 
        because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, 
        by reproduction

    First Milestone:
        Build a data structure to store the board state
        “Pretty-print” the board to the terminal
        Given a starting board state, calculate the next one
        Run the game forever

    Then some extensions:
    
        Save interesting starting positions to files and add the ability to reload them into your Life
        Improve the User Interface
        Change the rules of Life

"""
from pprint import pprint as pp
from random import random

def random_state(cols, rows, freq):
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


def next_state(init_state):
    """
        TO BORN any dead cell has to have 3 live neighbors
        [0, 0, 1, 0, 0] , [0, 0, 1, 0, 0] 
        [0, 0, 1, 0, 0]
        [0, 0, 1, 0, 0]
IF alive:
    if count(1) <= 1:
        alive is dead 

        [0, 0, 0, 0, 0] 
        [0, 1, 1, 1, 0]
        [0, 0, 0, 0, 0]
        If any live (#) cell has 0 or 1 live neighbors it DIES (" ")
        If any live (#) cell has 2 or 3 live neighbors it stays ALIVE 
        If any live (#) cell has more than 3 live neighbors stays ALIVE
            by reproduction
        If any dead cell (" ") has ecactly 3 live neighbors it becomes
            ALIVE ("#")
        
        If any dead cell.neighbors == 3:
            it becomes alive 
        If live cell have 0 or 1 live neighbors:
            cell becomes dead 
        If live cell have 2 or 3 live neighbors:
            it stays alive 
        If live cell have more than 3 live neighbors:
            reproduction 

        I should create a new new_state

    new_state = []
    for row in init_state:
        return 
        adjacent_state = []
        find all values TODO:  
    """

def render(board_state):
    print("----------GAME OF LIFE----------")
    for row in board_state:
        arr = []
        for cell in row: 
            if cell == 1:
                arr.append("#")
            else:
                arr.append(" ")
        pp(arr)
        arr.clear()

a_random_state = random_state(5, 8, 0.5)
render(a_random_state)
render(random_state(12, 30, 0.5))

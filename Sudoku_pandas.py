import pandas as pd

def isunique(lists):
    if [1,2,3,4,5,6,7,8,9] != sorted(lists):
        return False
    return True

def check_columns(grid_sudoku):
    for i in range(9):
        column = grid_sudoku.iloc[:, i]
        if isunique(column) != True:            
            return False
    return True 

def check_line(grid_sudoku):
    for i in range(9):
        line = grid_sudoku.iloc[i, :]
        if isunique(line) != True:            
            return False
    return True 

def check_sudoku(grid_sudoku):
    if check_line(grid_sudoku):
        if check_columns(grid_sudoku):
            if check_square(grid_sudoku):
                return True
    return False

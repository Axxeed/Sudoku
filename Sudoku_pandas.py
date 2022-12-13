import numpy as np
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
        line = grille_sudoku.iloc[i, :]
        if isunique(line) != True:
             return False
        return True

def check_square(grid_sudoku):
    square = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            for x in range(i,i+3):
                for y in range(j,j+3):
                    first = grid_sudoku[x][y]
                    square.append(first)
            if isunique(square) == True:
                square = []
            else:
                print(square)
                return False
    return True


def check_sudoku(grid_sudoku):
    if check_line(grid_sudoku) == True:
        if check_columns(grid_sudoku) == True:
            if check_square(grid_sudoku) == True:
                return True
    return False
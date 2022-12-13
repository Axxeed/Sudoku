import numpy as np

# Fonction qui regarde si toute les valeur sont bien unique sur une ligne
def check_rows(grid):
    for i in range(9):
        if len(set(grid[i])) != 9:
            return False
    return True

# Fonction qui regarde si toutes les valeur sont bien unique sur une colonne
def check_columns(grid):
    col = grid.transpose()
    for i in range(9):
        if len(set(col[i])) != 9:
            return False
    return True

# Fonction qui regarde si les valeur des sous grilles sont bien unique
def check_square(grid):
      for i in range(9):
        subgrid = grid[i//3*3:i//3*3+3, i%3*3:i%3*3+3].flatten()
        if len(set(subgrid)) != 9:
              return False
        else:
            return True

# Fonction qui appelle toute les autres afin de verifier tout le sudoku
def check_sudoku(grid):
    grid = np.array(grid)
    if check_rows(grid) == True:
        if check_columns(grid) == True:
            if check_square(grid) == True:
                return True
    return False
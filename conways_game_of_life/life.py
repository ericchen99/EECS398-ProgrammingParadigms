from pprint import pprint
from time import sleep
from copy import deepcopy
from pdb import set_trace
def simulate(rows, cols, steps, live_cells):
    """Run Conway's Game of Life on a finite (rows x cols) grid.

    Runs the simulation for the number of time steps specified by
    the steps parameter. Initializes the grid such that all cells
    are dead except those listed in live_cells, which should be a
    sequence of (row, column) pairs. Prints the grid after each
    time step.
    """

    # Initialize live_cells grid
    grid = [[0 for i in range(cols + 2)] for j in range(rows + 2)]
    for r, c in live_cells:
        grid[r + 1][c + 1] = 1

    print_grid(grid)

    # Iterate over steps
    for _ in range(steps):
        grid2 = deepcopy(grid)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # Count Live Neighbors
                live_neighbors = 0
                relative_neighbor_idx = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
                for n1, n2 in relative_neighbor_idx:
                    if grid[r + n1][c + n2]:
                        live_neighbors += 1

                # Any live cell with two or three live neighbours survives. All other live cells die in the next generation. 
                if grid[r][c] and live_neighbors != 2 and live_neighbors != 3:
                    grid2[r][c] = 0
                
                # Any dead cell with three live neighbours becomes a live cell. All other dead cells stay dead.
                if not grid[r][c] and live_neighbors == 3:
                    grid2[r][c] = 1

        # Print grid
        print_grid(grid2)
        grid = grid2
        sleep(0.2)

def print_grid(grid):
    rows, cols = len(grid), len(grid[0])
    print('-' * cols)

    for r in range(rows):
        if r == 0 or r == rows - 1: continue

        print('|', end='')
        for c in range(cols):
            if c == 0 or c == cols - 1: continue

            if grid[r][c]:
                print('*', end='')
            else:
                print(' ', end='')
        print('|')
    print('-' * cols)
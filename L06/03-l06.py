def minesweeper(rows, cols, mines):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row, col in mines:
        grid[row][col] = 'X'

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 'X':
                count = 0
                for i in range(max(0, row-1), min(rows, row+2)):
                    for j in range(max(0, col-1), min(cols, col+2)):
                        if grid[i][j] == 'X':
                            count += 1
                grid[row][col] = count

    return grid

def transpose(grid):
    return list(map(list, zip(*grid)))

def grids(grid):
    for row in grid:
        print(' '.join(map(str, row)))

rows, cols = map(int, input("Grid Size: ").split())
num_mines = int(input("Number of mine(s): "))
mines = [list(map(int, input(f"Mine#{i+1}: ").split())) for i in range(num_mines)]

grid = minesweeper(rows, cols, mines)
transposed_grid = transpose(grid)
grids(transposed_grid)














SIGMA                          # type: ignore
def count_destroyed_enemies(grid, n):
    destroyed_count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'G':
                for di in range(-2, 3):
                    for dj in range(-2, 3):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 'E':
                            destroyed_count += 1
                            grid[ni][nj] = '.'

    return destroyed_count

n = int(input().strip())

grid = []
for _ in range(n):
    grid.append(list(input().strip()))


print(count_destroyed_enemies(grid, n))

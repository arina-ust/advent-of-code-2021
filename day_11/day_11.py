import common

n_grid = 10
n_steps = 100


def day_11_1(path):
    grid = common.read_int_list_of_lists(path)

    n_flashes = 0

    for step in range(n_steps):

        for y in range(n_grid):
            for x in range(n_grid):
                grid[y][x] += 1

        for y in range(n_grid):
            for x in range(n_grid):
                octopus = grid[y][x]

                if octopus > 9:

                    left = x - 1
                    right = x + 1
                    up = y - 1
                    down = y + 1

                    if left >= 0:
                        grid[y][left] += 1
                    if left >= 0 and up >= 0:
                        grid[up][left] += 1
                    if up >= 0:
                        grid[up][x] += 1
                    if up >= 0 and right < n_grid:
                        grid[up][right] += 1
                    if right < n_grid:
                        grid[y][right] += 1
                    if right < n_grid and down < n_grid:
                        grid[down][right] += 1
                    if down < n_grid:
                        grid[down][x] += 1
                    if down < n_grid and left >= 0:
                        grid[down][left] += 1

        for y in range(n_grid):
            for x in range(n_grid):
                octopus = grid[y][x]
                if octopus > 9:
                    n_flashes += 1
                    grid[y][x] = 0

    return n_flashes

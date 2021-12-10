import common


def day_9_1(path):
    local_mins = find_local_mins(path)

    print(local_mins)

    return sum([x + 1 for x in local_mins])


def find_local_mins(path):
    grid = common.read_int_list_of_lists(path)
    local_mins = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            e = grid[y][x]
            left = x - 1
            right = x + 1
            up = y - 1
            down = y + 1
            neighbors = []
            if left >= 0:
                neighbors.append(grid[y][left])
            if right < len(grid[0]):
                neighbors.append(grid[y][right])
            if up >= 0:
                neighbors.append(grid[up][x])
            if down < len(grid):
                neighbors.append(grid[down][x])

            m = min(neighbors)
            if e < m:
                local_mins.append(e)
    return local_mins


def day_9_2(path):
    local_mins = find_local_mins(path)

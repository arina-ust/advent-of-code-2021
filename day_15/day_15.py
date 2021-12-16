import sys

import common


def day_15_1(path):
    grid = common.read_int_list_of_lists(path)
    n = len(grid)

    return find_min_risk(grid, n)


def find_min_risk(grid, n):
    max_value = sys.maxsize
    shortest_path = {}
    unvisited = []
    for i in range(n):
        for j in range(n):
            shortest_path[(j, i)] = max_value
            unvisited.append((j, i))
    shortest_path[(0, 0)] = 0
    previous = {}
    while unvisited:
        lightest = None
        for coords in unvisited:
            if lightest is None:
                lightest = coords
            elif shortest_path[coords] < shortest_path[lightest]:
                lightest = coords

        neighbors = []
        x, y = lightest
        if x + 1 < n:
            neighbors.append((x + 1, y))
        if x - 1 >= 0:
            neighbors.append((x - 1, y))
        if y + 1 < n:
            neighbors.append((x, y + 1))
        if y - 1 >= n:
            neighbors.append((x, y - 1))

        for neighbor in neighbors:
            candidate = shortest_path[lightest] + grid[neighbor[1]][neighbor[0]]
            if candidate < shortest_path[neighbor]:
                shortest_path[neighbor] = candidate
                previous[neighbor] = lightest

        unvisited.remove(lightest)
    return shortest_path[(n - 1, n - 1)]


def day_15_2(path):
    grid = common.read_int_list_of_lists(path)
    n = len(grid)

    for row in range(n):
        c = 0
        for i in range(n, n*5, n):
            c += 1
            for j in range(i, i+n):
                k = j - int(i / c)
                value = grid[row][k] + 1
                if value > 9:
                    value = 1
                grid[row].append(value)

    new_n = len(grid[0])
    j = 0
    while j < new_n - n:
        row = j
        new_row = []
        for v in grid[row]:
            value = v + 1
            if value > 9:
                value = 1
            new_row.append(value)
        grid.append(new_row)
        j += 1

    return find_min_risk(grid, new_n)


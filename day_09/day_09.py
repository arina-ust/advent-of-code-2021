import common


def day_9_1(path):
    grid = common.read_int_list_of_lists(path)
    local_mins = find_local_mins(grid)[0]

    print(local_mins)

    return sum([x + 1 for x in local_mins])


def find_local_mins(grid):
    local_mins = []
    coords = []
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
                coords.append((x, y))
    return local_mins, coords


def day_9_2(path):
    grid = common.read_int_list_of_lists(path)
    local_mins_coords = find_local_mins(grid)[1]

    basins_size = []
    for c in local_mins_coords:
        basin = []
        find_basin(grid, c, basin, {})
        s = len(basin)

        if len(basins_size) < 3:
            basins_size.append(s)
            continue

        search = [b for b in basins_size]
        search.append(s)
        m = min(search)
        if m == s:
            continue
        basins_size.remove(m)
        basins_size.append(s)

    return basins_size[0] * basins_size[1] * basins_size[2]


def find_basin(grid, start_coord, basin_values, seen_coords: dict):
    x = start_coord[0]
    y = start_coord[1]

    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or start_coord in seen_coords:
        return

    seen_coords[start_coord] = True

    e = grid[y][x]
    if e == 9:
        return

    basin_values.append(e)

    find_basin(grid, (x-1, y), basin_values, seen_coords)
    find_basin(grid, (x+1, y), basin_values, seen_coords)
    find_basin(grid, (x, y-1), basin_values, seen_coords)
    find_basin(grid, (x, y+1), basin_values, seen_coords)

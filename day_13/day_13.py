import common


def day_13_1(path):
    all_input = common.read_string_list(path)

    coordinates = []
    instructions = []

    read_input(all_input, coordinates, instructions)

    max_x, max_y = find_max(coordinates)

    grid = create_grid(max_x, max_y)

    for point in coordinates:
        grid[point.y][point.x] = 1

    # first fold y in easy, x in full
    fold = instructions[0]
    coord = fold.coord
    max_x_next = max_x
    max_y_next = max_y
    if fold.is_along_y():
        add_to_y = coord - 1
        for y in range(coord+1, max_y_next+1):
            for x in range(max_x+1):   # ???
                point_to_disappear = grid[y][x]
                point_to_add = grid[add_to_y][x]
                if point_to_add == 0:
                    grid[add_to_y][x] += point_to_disappear
                grid[y][x] = 0
            add_to_y -= 1
        max_y_next = coord - 1
    else:
        for y in range(max_y+1):  # ???
            add_to_x = coord - 1
            for x in range(coord + 1, max_x_next + 1):
                point_to_disappear = grid[y][x]
                point_to_add = grid[y][add_to_x]
                if point_to_add == 0:
                    grid[y][add_to_x] += point_to_disappear
                grid[y][x] = 0
                add_to_x -= 1
        max_x_next = coord - 1

    return count_dots(grid)


def count_dots(grid):
    count = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            count += grid[j][i]
    return count


def create_grid(max_x, max_y):
    grid = []
    for y in range(max_y+1):
        coords = []
        for x in range(max_x+1):
            coords.append(0)
        grid.append(coords)
    return grid


def find_max(coordinates):
    max_x, max_y = 0, 0
    for point in coordinates:
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)
    return max_x, max_y


def read_input(all_input, coordinates, instructions):
    instructions_on = False
    for e in all_input:
        if len(e.strip()) == 0:
            instructions_on = True
            continue
        if instructions_on:
            instruction, coord = e.strip().split("=")
            instructions.append(Instruction(instruction[-1], int(coord)))
        else:
            x, y = e.strip().split(",", 2)
            coordinates.append(common.Point(int(x), int(y)))


class Instruction:

    def __init__(self, direction:str, coord: int):
        self.direction = direction
        self.horizontal = direction == "y"
        self.vertical = direction == "x"
        self.coord = coord

    def is_along_x(self):
        return self.vertical

    def is_along_y(self):
        return self.horizontal

    def __str__(self):
        return 'Instruction({self.direction}={self.coord})'.format(self=self)

    def __repr__(self):
        return str(self)

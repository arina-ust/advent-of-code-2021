import common


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

    def __repr__(self):
        return str(self)


class Line:

    def __init__(self, string_repr: str):
        points = string_repr.split("->")
        x1, y1 = points[0].strip().split(",")
        x2, y2 = points[1].strip().split(",")

        self.start = Point(int(x1), int(y1))
        self.end = Point(int(x2), int(y2))

        self.min_x = min(self.start.x, self.end.x)
        self.max_x = max(self.start.x, self.end.x)
        self.min_y = min(self.start.y, self.end.y)
        self.max_y = max(self.start.y, self.end.y)

    def __str__(self):
        return '|{self.start} -> {self.end}|'.format(self=self)

    def __repr__(self):
        return str(self)

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_horizontal(self):
        return self.start.y == self.end.y

    def get_all_points(self):
        if self.is_horizontal():
            return [Point(x, self.start.y) for x in range(self.min_x, self.max_x+1)]
        elif self.is_vertical():
            return [Point(self.start.x, y) for y in range(self.min_y, self.max_y+1)]
        else:
            result = []
            x = self.start.x
            y = self.start.y
            if x == self.min_x and y == self.min_y:
                while x <= self.end.x and y <= self.end.y:
                    result.append(Point(x, y))
                    x += 1
                    y += 1
            elif x == self.max_x and y == self.max_y:
                while x >= self.end.x and y >= self.end.y:
                    result.append(Point(x, y))
                    x -= 1
                    y -= 1
            elif x == self.max_x and y == self.min_y:
                while x >= self.end.x and y <= self.end.y:
                    result.append(Point(x, y))
                    x -= 1
                    y += 1
            else:
                while x <= self.end.x and y >= self.end.y:
                    result.append(Point(x, y))
                    x += 1
                    y -= 1
            return result


def day_5(path, is_part_one):
    lines = [Line(s) for s in common.read_string_list(path)]

    max_x, max_y = get_max_coordinates(lines)
    print("max x = ", max_x)
    print("max y = ", max_y)

    area = get_empty_area(max_x, max_y)

    for line in lines:
        if is_part_one and (not (line.is_horizontal() or line.is_vertical())):
            continue
        for point in line.get_all_points():
            area[point.y][point.x] += 1

    return get_number_dangerous_points(area, max_x, max_y)


def get_max_coordinates(lines):
    all_x, all_y = [line.max_x for line in lines], [line.max_y for line in lines]
    return max(all_x), max(all_y)


def get_empty_area(max_x, max_y):
    area = []
    for x in range(max_x + 1):
        area.append([0] * (max_y + 1))
    return area


def get_number_dangerous_points(area, max_x, max_y):
    count_more_than_2 = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if area[y][x] > 1:
                count_more_than_2 += 1
    return count_more_than_2

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
            min_x = min(self.start.x, self.end.x)
            max_x = max(self.start.x, self.end.x)
            return [Point(x, self.start.y) for x in range(min_x, max_x+1)]
        elif self.is_vertical():
            min_y = min(self.start.y, self.end.y)
            max_y = max(self.start.y, self.end.y)
            return [Point(self.start.x, y) for y in range(min_y, max_y+1)]
        else:
            pass


def day_5_1(path):
    lines = [Line(s) for s in common.read_string_list(path)]
    # print(lines)

    all_x, all_y = [], []
    for line in lines:
        all_x.append(line.start.x)
        all_x.append(line.end.x)
        all_y.append(line.start.y)
        all_y.append(line.end.y)
    max_x = max(all_x)
    max_y = max(all_y)
    print("max x = ", max_x)
    print("max y = ", max_y)

    area = []
    for x in range(max_x+1):
        area.append([0]*(max_y+1))
    # print(area)

    for line in lines:
        if not (line.is_horizontal() or line.is_vertical()):
            # print(line.get_all_points())
            continue
        # print(line.get_all_points())
        for point in line.get_all_points():
            area[point.y][point.x] += 1
    # print(area)

    count_more_than_2 = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if area[y][x] > 1:
                count_more_than_2 += 1
    return count_more_than_2

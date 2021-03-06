

def read_int_list(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
    return lines


def read_comma_sep_int_list(path):
    with open(path) as file:
        line = file.readlines()[0]
        line = [int(value.rstrip()) for value in line.split(",")]
    return line


def read_string_list(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def read_int_list_of_lists(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [[int(c) for c in line.rstrip()] for line in lines]
    return lines


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

    def __repr__(self):
        return str(self)

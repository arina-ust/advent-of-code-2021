import common


def day_2_1(path):
    lines = common.read_string_list(path)
    lines = [tuple(line.split(" ")) for line in lines]
    h, d = 0, 0
    for t in lines:
        command = t[0]
        value = int(t[1])
        if command == "forward":
            h += value
        elif command == "down":
            d += value
        elif command == "up":
            d -= value
    return h*d


def day_2_2(path):
    lines = common.read_string_list(path)
    lines = [tuple(line.split(" ")) for line in lines]
    aim, h, d = 0, 0, 0
    for t in lines:
        command = t[0]
        value = int(t[1])
        if command == "forward":
            h += value
            d += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    return h * d

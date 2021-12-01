from common import read_int_list


def day_1_1(path):
    lines = read_int_list(path)
    count = 0
    for i in range(0, len(lines) - 1):
        if lines[i+1] > lines[i]:
            count += 1
    return count


def day_1_2(path):
    lines = read_int_list(path)
    count = 0
    for i in range(0, len(lines) - 3):
        sum_first_window = lines[i] + lines[i+1] + lines[i+2]
        sum_second_window = lines[i+1] + lines[i+2] + lines[i+3]
        if sum_second_window > sum_first_window:
            count += 1
    return count

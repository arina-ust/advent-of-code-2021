import copy

import common


def day_3_1(path):
    columns = list(zip(*common.read_string_list(path)))
    limit = len(columns[0]) / 2
    gamma_bin, epsilon_bin = "0b", "0b"
    for c in columns:
        s = sum([int(x) for x in c])
        if s > limit:
            gamma_bin += "1"
            epsilon_bin += "0"
        else:
            gamma_bin += "0"
            epsilon_bin += "1"
    return int(gamma_bin, 2) * int(epsilon_bin, 2)


def day_3_2(path):
    lines = common.read_string_list(path)
    oxygen = get_meter(lines, True)
    scrubber = get_meter(lines, False)
    return int(oxygen[0], 2) * int(scrubber[0], 2)


def get_meter(lines, is_oxygen):
    meter = copy.deepcopy(lines)
    for j in range(len(lines[0])):
        start_zero, start_one = [], []
        for value in meter:
            if value[j] == "1":
                start_one.append(value)
            else:
                start_zero.append(value)
        if len(start_one) >= len(start_zero):
            if is_oxygen:
                meter = start_one
            else:
                meter = start_zero
        else:
            if is_oxygen:
                meter = start_zero
            else:
                meter = start_one
        if len(meter) == 1:
            return meter
    raise ValueError("no values left in the meter")

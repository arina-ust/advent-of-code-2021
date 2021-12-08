import common


def day_8_1(path):
    digits_len = {2: 1, 4: 4, 3: 7, 7: 8}  # length to digit
    outputs = [line.strip().split("|")[1].strip() for line in common.read_string_list(path)]

    outputs = [i for output in outputs for i in output.split(" ")]

    count = 0
    for o in outputs:
        if len(o) in digits_len:
            count += 1
    return count

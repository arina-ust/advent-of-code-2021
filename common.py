

def read_int_list(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
    return lines

import common

conversion = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def day_16_1(path):
    signal = common.read_string_list(path)[0]

    bin_signal = ''
    for ch in signal:
        bin_signal += conversion[ch]

    versions = []
    unpack(bin_signal, versions)
    print(versions)
    return sum(versions)


def unpack(bin_signal, versions):
    if len(bin_signal) < 11:
        return

    i = 0
    if i + 3 >= len(bin_signal):
        return
    v_i = i + 3
    t_i = v_i + 3

    version = int(bin_signal[i:v_i], 2)
    versions.append(version)

    type_id = int(bin_signal[v_i:t_i], 2)
    is_literal = type_id == 4
    if is_literal:
        number = ''
        j = t_i
        while j < len(bin_signal):
            number += bin_signal[j + 1:j + 5]
            is_last_group = bin_signal[j] == '0'
            j += 5
            if is_last_group:
                break

        print("found literal value", int(number, 2))
        i = j
        unpack(bin_signal[i:], versions)
    else:  # is an operator packet
        length_type_id = bin_signal[t_i]
        is_bits_length = length_type_id == '0'
        if is_bits_length:
            length_in_bits = bin_signal[t_i + 1:t_i + 16]
            length_int = int(length_in_bits, 2)
            print("found operator 15 bit packet with length of subpackets in bits", length_int)
            unpack(bin_signal[t_i+16:], versions)
        else:  # is number of packets
            length_in_packets = bin_signal[t_i + 1:t_i + 12]
            length_int = int(length_in_packets, 2)
            print("found operator 11 bit packet with number of subpackets", length_int)
            start = t_i + 1
            unpack(bin_signal[start + 11:], versions)  # TODO: how to come out of it? return from the "literal number" case as it's always a leaf?


def day_16_2(path):
    signal = common.read_string_list(path)[0]

    bin_signal = ''
    for ch in signal:
        bin_signal += conversion[ch]

    operations = []
    unpack_with_operations(bin_signal, operations)
    print(operations)

    result = 0
    i = len(operations) - 1
    while i > 0:
        right = operations[i]
        left = operations[i - 1]
        if right not in types_to_operators.values():  # it's a literal number
            if left not in types_to_operators.values():  # it's also a literal number
                op = operations[i - 2]
                result = apply_op(op, left, right)
            else:
                op = left
                if op == "sum_op":
                    result = apply_op(op, 0, right)
                elif op == "product":
                    result = apply_op(op, 1, right)
                else:
                    raise ValueError("should not be here?")
        else:  # right is an operator




def apply_op(op, left, right):
    if op == "sum_op":
        return sum(left, right)
    elif op == "product":
        return left * right
    elif op == "min_op":
        return min(left, right)
    elif op == "max_op":
        return max(left, right)
    elif op == "greater":
        if left > right:
            return 1
        else:
            return 0
    elif op == "less":
        if left < right:
            return 1
        else:
            return 0
    elif op == "equal":
        if left == right:
            return 1
        else:
            return 0
    else:
        raise ValueError("unknown op")


types_to_operators = {
    0: "sum_op",
    1: "product",
    2: "min_op",
    3: "max_op",
    5: "greater",
    6: "less",
    7: "equal"
}


def sum_op(left, right):
    return left + right


def unpack_with_operations(bin_signal, operations):
    if len(bin_signal) < 11:
        return

    i = 0
    if i + 3 >= len(bin_signal):
        return
    v_i = i + 3
    t_i = v_i + 3

    version = int(bin_signal[i:v_i], 2)

    type_id = int(bin_signal[v_i:t_i], 2)
    is_literal = type_id == 4
    if is_literal:
        number = ''
        j = t_i
        while j < len(bin_signal):
            number += bin_signal[j + 1:j + 5]
            is_last_group = bin_signal[j] == '0'
            j += 5
            if is_last_group:
                break

        literal_value = int(number, 2)
        print("found literal value", literal_value)
        i = j
        operations.append(literal_value)
        unpack_with_operations(bin_signal[i:], operations)
    else:  # is an operator packet
        operator = types_to_operators[type_id]
        length_type_id = bin_signal[t_i]
        is_bits_length = length_type_id == '0'
        operations.append(operator)
        if is_bits_length:
            length_in_bits = bin_signal[t_i + 1:t_i + 16]
            length_int = int(length_in_bits, 2)
            print("found operator 15 bit packet with length of subpackets in bits", length_int)
            unpack_with_operations(bin_signal[t_i+16:], operations)
        else:  # is number of packets
            length_in_packets = bin_signal[t_i + 1:t_i + 12]
            length_int = int(length_in_packets, 2)
            print("found operator 11 bit packet with number of subpackets", length_int)
            start = t_i + 1
            unpack_with_operations(bin_signal[start + 11:], operations)  # TODO: how to come out of it? return from the "literal number" case as it's always a leaf?













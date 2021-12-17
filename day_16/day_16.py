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
        # while (i % 4) != 0:
        #     i += 1
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
            # for p in range(1, length_int+1):
            unpack(bin_signal[start + 11:], versions)  # TODO: how to come out of it? return from the "literal number" case as it's always a leaf?
            i = start + 11 * length_int + 11















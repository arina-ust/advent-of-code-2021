import common


def day_8_1(path):
    outputs = [line.strip().split("|")[1].strip() for line in common.read_string_list(path)]

    outputs = [i for output in outputs for i in output.split(" ")]

    count = 0
    for o in outputs:
        if len(o) in digits_len:
            count += 1
    return count


digits_len = {2: 1, 4: 4, 3: 7, 7: 8}  # length to digit


# max chars = 7 -> 8 [1,4,7,8]
# compare 7 and 1 -> h1 (uncommon)
# compare 9 and 4 -> h3 (remove all 4 and h1)
# len(5) and compare each to 1 -> contains 1 = 3 [1,3,4,7,8,]
# compare 3 and 1 -> h2 (remove all 1 and h1, h3)
# 8 minus h2 -> 0 [0,1,3,4,7,8]
# compare 4 and 1 -> v1 (remove h2, uncommon)
# len(5) and compare 2 and 5 -> check for v1 exists -> found 2 and 5 [0,1,2,3,4,5,7,8]
# compare 1 and 5 -> v4 (remove h1, h2, h3, v1 from 5 and compare to 1)
# remove v4 from 1 -> v2
# remove all found from 8 -> v3
# len(6) and has v2 -> 9 [0,1,2,3,4,5,7,8,9]
# remaining len(6) -> 6 [0,1,2,3,4,5,6,7,8,9]

def day_8_2(path):
    task = [line.strip() for line in common.read_string_list(path)]

    inputs, outputs = [], []

    for line in task:
        arr = line.split("|")
        inputs.append(arr[0].strip().split(" "))
        outputs.append(arr[1].strip().split(" "))

    sum_output = 0
    for i in range(len(inputs)):
        result_seg = {"h1": '', "h2": '', "h3": '', "v1": '', "v2": '', "v3": '', "v4": ''}
        result_digit = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        len_six = []
        len_five = []
        to_decode = inputs[i]
        for signal in to_decode:
            len_sig = len(signal)
            if len_sig in digits_len:
                result_digit[digits_len[len_sig]] = sorted(signal)  # [1,4,7,8] []
            if len(signal) == 5:
                len_five.append(signal)
            if len(signal) == 6:
                len_six.append(signal)

        result_seg["h1"] = set(result_digit[7]).difference(set(result_digit[1])).pop()  # [1,4,7,8] [h1]

        for e in len_six:
            res = set(e).difference(set(result_digit[4]))
            res = res.difference(set(result_seg["h1"]))
            if len(res) == 1:
                result_seg["h3"] = res.pop()
                result_digit[9] = sorted(e)  # [1,4,7,8,9] [h1, h3]

        for e in len_five:
            res = set(e).intersection(set(result_digit[1]))
            if len(res) == 2:
                result_digit[3] = sorted(e)  # [1,3,4,7,8,9] [h1, h3]

        three_minus_one = set(result_digit[3]).difference(set(result_digit[1]))
        # print(result_seg)
        minus_known = three_minus_one.difference({result_seg["h1"], result_seg["h3"]})
        result_seg["h2"] = minus_known.pop()
        # [1,3,4,7,8,9] [h1, h2, h3]

        result_digit[0] = sorted(set(result_digit[8]).difference(set(result_seg["h2"])))  # [0,1,3,4,7,8,9] [h1, h2, h3]

        result_seg["v1"] = set(result_digit[4]).difference(set(result_digit[1])).difference(set(result_seg["h2"])).pop()
        # [0,1,3,4,7,8,9] [h1, h2, h3, v1]

        for e in len_five:
            if sorted(e) == result_digit[3]:
                continue
            if len(set(e).union(set(result_seg["v1"]))) == 5:
                result_digit[5] = sorted(e)
            else:
                result_digit[2] = sorted(e)
        # [0,1,2,3,4,5,7,8,9] [h1, h2, h3, v1]

        result_seg["v4"] = set(result_digit[1]).intersection(set(result_digit[5]).difference(
            {result_seg["h1"], result_seg["h2"], result_seg["h3"], result_seg["v1"]})).pop()
        # [0,1,2,3,4,5,7,8,9] [h1, h2, h3, v1, v4]

        result_seg["v2"] = set(result_digit[1]).difference(set(result_seg["v4"])).pop()
        # [0,1,2,3,4,5,7,8,9] [h1, h2, h3, v1, v2, v4]

        result_seg["v3"] = set(result_digit[8]).difference({result_seg["h1"], result_seg["h2"], result_seg["h3"],
                                                            result_seg["v1"], result_seg["v2"], result_seg["v4"]}).pop()
        # [0,1,2,3,4,5,7,8,9] [h1, h2, h3, v1, v2, v3, v4]

        for e in len_six:
            if sorted(e) == result_digit[0] or sorted(e) == result_digit[9]:
                continue
            else:
                result_digit[6] = sorted(e)  # [0,1,2,3,4,5,6,7,8,9] [h1, h2, h3, v1, v2, v3, v4]

        # print(result_digit)
        # print(result_seg)

        result_v_to_d = {''.join(v): k for k, v in result_digit.items()}
        # print(result_v_to_d)

        output = [''.join(sorted(o)) for o in outputs[i]]
        # print(output)

        result = ""
        for signal in output:
            result += str(result_v_to_d[signal])

        # print(result)
        sum_output += int(result)
    return sum_output

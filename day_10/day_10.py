import common


closing_to_opening = {")": "(", "]": "[", "}": "{", ">": "<"}
opening_to_closing = {"(": ")", "[": "]", "{": "}", "<": ">"}


def day_10_1(path):
    lines = get_input_lines(path)

    score = {")": 3, "]": 57, "}": 1197, ">": 25137}

    seen_closing_wrong = {")": 0, "]": 0, "}": 0, ">": 0}
    corrupted_lines = {}

    for k in range (len(lines)):
        line = lines[k]
        i = 0
        while i < (len(line) - 1):
            if i < 0:
                i = 0
            c = line[i]
            next_c = line[i + 1]
            if c in opening_to_closing and next_c in opening_to_closing:
                i += 1
                continue
            if c in opening_to_closing and next_c in closing_to_opening:
                if opening_to_closing[c] == next_c:
                    line[i] = "*"
                    line[i + 1] = "*"
                    line.remove("*")
                    line.remove("*")
                    i -= 1
                else:
                    seen_closing_wrong[next_c] += 1
                    corrupted_lines[k] = True
                    break

    return seen_closing_wrong[")"] * score[")"] + seen_closing_wrong["]"] * score["]"] + \
           seen_closing_wrong["}"] * score["}"] + seen_closing_wrong[">"] * score[">"], corrupted_lines


def get_input_lines(path):
    lines = common.read_string_list(path)
    lines = [[c for c in line.strip()] for line in lines]
    return lines


def day_10_2(path):
    lines = get_input_lines(path)

    corrupted_lines = day_10_1(path)[1]
    points = {")": 1, "]": 2, "}": 3, ">": 4}

    completions = []

    for k in range(len(lines)):
        if k in corrupted_lines:
            continue

        line = lines[k]
        i = 0
        while i < (len(line) - 1):
            if i < 0:
                i = 0
            c = line[i]
            next_c = line[i + 1]
            if c in opening_to_closing and next_c in opening_to_closing:
                i += 1
                continue
            if c in opening_to_closing and next_c in closing_to_opening:
                if opening_to_closing[c] == next_c:
                    line[i] = "*"
                    line[i + 1] = "*"
                    line.remove("*")
                    line.remove("*")
                    i -= 1
        result = ''
        for j in range(len(line)-1, -1, -1):
            result += opening_to_closing[line[j]]
        completions.append(result)

    return calculate_middle_score(completions, points)


def calculate_middle_score(completions, points):
    scores = []
    for completion in completions:
        score = 0
        for c in completion:
            score = score * 5 + points[c]
        scores.append(score)
    scores = sorted(scores)
    middle = int(len(scores) / 2)
    score = scores[middle]
    return score

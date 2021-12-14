import sys

import common


def day_14_1(path):
    lines = common.read_string_list(path)
    template = lines[0]
    insertion_rules = get_rules_dict(lines[2:])
    letter_counts = get_counts(template)
    n_steps = 10

    polymer = template
    for step in range(n_steps):
        step_result = ''
        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            result = insertion_rules[pair]
            if i == len(polymer) - 2:  # last pair
                step_result += result
            else:
                step_result += result[:-1]
            increase_count(result[1], letter_counts)
        polymer = step_result

    min_counts = sys.maxsize
    max_counts = 0
    for count in letter_counts.values():
        min_counts = min(min_counts, count)
        max_counts = max(max_counts, count)

    return max_counts - min_counts


def get_rules_dict(lines):
    rules = {}
    for line in lines:
        parts = [p.strip() for p in line.split(" -> ")]
        result = parts[0][0] + parts[1] + parts[0][1]
        rules[parts[0]] = result
    return rules


def get_counts(template):
    letter_counts = {}
    for letter in template:
        increase_count(letter, letter_counts)
    return letter_counts


def increase_count(letter, letter_counts):
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

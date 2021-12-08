import sys

import common


def day_7_1(path):
    positions = common.read_comma_sep_int_list(path)
    min_p = min(positions)
    max_p = max(positions)
    min_fuel = sys.maxsize
    best_p = 0
    for i in range (min_p, max_p+1):
        fuel_sum = 0
        for crab_p in positions:
            fuel = abs(i - crab_p)
            fuel_sum += fuel
        if fuel_sum < min_fuel:
            min_fuel = fuel_sum
            best_p = i
    print("best position", best_p)
    return min_fuel


def day_7_2(path):
    positions = common.read_comma_sep_int_list(path)
    min_p = min(positions)
    max_p = max(positions)
    min_fuel = sys.maxsize
    best_p = 0
    for i in range (min_p, max_p+1):
        fuel_sum = 0
        for crab_p in positions:
            fuel = abs(i - crab_p)
            new_fuel = 0
            for f in range(fuel):
                new_fuel += (f+1)
            fuel_sum += new_fuel
        if fuel_sum < min_fuel:
            min_fuel = fuel_sum
            best_p = i
    print("best position", best_p)
    return min_fuel

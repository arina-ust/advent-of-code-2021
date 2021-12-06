import common


def day_6_1(path):
    fish = common.read_comma_sep_int_list(path)
    new_fish = []
    # n_days = 18
    n_days = 80
    for d in range(n_days):
        new_fish.clear()
        for i in range(len(fish)):
            f = fish[i]
            if f == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1
        for n in new_fish:
            fish.append(n)
    return len(fish)


def day_6_2(path):
    fish_input = common.read_comma_sep_int_list(path)
    m = {}
    for f in fish_input:
        if f in m:
            m[f] += 1
        else:
            m[f] = 1
    for d_to_birth in range(0, 9):
        if d_to_birth not in m:
            m[d_to_birth] = 0

    # n_days = 18
    # n_days = 80
    n_days = 256

    for d in range(1, n_days+1):
        num_fish_to_give_birth = 0
        for d_to_birth in range(0, 9):
            if d_to_birth == 0:
                num_fish_to_give_birth = m[d_to_birth]
            else:
                new_days_to_birth = d_to_birth - 1
                n_fish = m[d_to_birth]
                m[d_to_birth] -= n_fish
                m[new_days_to_birth] += n_fish
        m[0] -= num_fish_to_give_birth
        m[6] += num_fish_to_give_birth
        m[8] += num_fish_to_give_birth

    count = 0
    for v in m.values():
        count += v
    return count

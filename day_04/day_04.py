
def day_4_1(path):
    dimension = 5
    numbers, boards, boards_visited = read_boards(path, dimension)
    found_winner = False
    winner = -1
    board_winner_index = -1
    for num in numbers:
        for board_index in range(len(boards)):
            for row_index in range(dimension):
                for n in range(dimension):
                    if num == boards[board_index][row_index][n]:
                        boards_visited[board_index][row_index][n] = 1
                        if sum(boards_visited[board_index][row_index]) == dimension or find_column_sum(boards_visited[board_index], dimension) == dimension:
                            found_winner = True
                            winner = num
                            board_winner_index = board_index
                            print("Won! With ", num, "on board #", board_winner_index)
                            break
                if found_winner:
                    break
            if found_winner:
                break
        if found_winner:
            break
    print(numbers)
    print(boards)
    print(boards_visited)

    board_winner, board_winner_visited = boards[board_winner_index], boards_visited[board_winner_index]
    sum_uncalled = 0
    for i in range(dimension):
        for j in range(dimension):
            if board_winner_visited[i][j] == 0:
                sum_uncalled += board_winner[i][j]
    print("Sum uncalled = ", sum_uncalled)
    return sum_uncalled * winner


def day_4_2(path):
    dimension = 5
    numbers, boards, boards_visited = read_boards(path, dimension)
    latest_winner = -1
    latest_board_winner_index = -1
    won_boards = set()
    for num in numbers:
        for board_index in range(len(boards)):
            if board_index in won_boards:
                continue
            for row_index in range(dimension):
                for n in range(dimension):
                    if num == boards[board_index][row_index][n]:
                        boards_visited[board_index][row_index][n] = 1
                        if sum(boards_visited[board_index][row_index]) == dimension or \
                                find_column_sum(boards_visited[board_index], dimension) == dimension:
                            latest_winner = num
                            latest_board_winner_index = board_index
                            won_boards.add(latest_board_winner_index)
    print(numbers)
    print(boards)
    print(boards_visited)
    print("Last board to win #", latest_board_winner_index)

    board_winner, board_winner_visited = boards[latest_board_winner_index], boards_visited[latest_board_winner_index]
    sum_uncalled = 0
    for i in range(dimension):
        for j in range(dimension):
            if board_winner_visited[i][j] == 0:
                sum_uncalled += board_winner[i][j]
    print("Sum uncalled = ", sum_uncalled)
    return sum_uncalled * latest_winner


def find_column_sum(board, dimension):
    column_sum = 0
    for n in range(dimension):
        for row_index in range(dimension):
            column_sum += board[row_index][n]
        if column_sum == dimension:
            return column_sum
        column_sum = 0
    return column_sum


def read_boards(path, dimension):
    numbers = []
    boards, boards_visited = [], []
    board, board_visited = [], []
    with open(path) as file:
        while line := file.readline():
            if len(numbers) == 0:
                numbers = [int(n) for n in line.split(",")]
                continue
            if len(line.strip()) == 0:
                board, board_visited = [], []
                boards.append(board)
                boards_visited.append(board_visited)
                continue
            row, row_visited = [], [0 for _ in range(dimension)]
            for n in line.rstrip().split(" "):
                if len(n) == 0:
                    continue
                s = n.strip()
                num = int(s)
                row.append(num)
            board.append(row)
            board_visited.append(row_visited)
    return numbers, boards, boards_visited

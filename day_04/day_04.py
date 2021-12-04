dimension = 5


def day_4_1(path):
    numbers, boards, boards_visited = read_boards(path)
    found_winner = False
    winner = -1
    board_winner_index = -1
    for num in numbers:
        for board_index in range(len(boards)):
            for row_index in range(dimension):
                for n in range(dimension):
                    if num == boards[board_index][row_index][n]:
                        boards_visited[board_index][row_index][n] = 1
                        if has_won(boards_visited[board_index], row_index, n):
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

    sum_uncalled = calculate_sum_uncalled(boards[board_winner_index], boards_visited[board_winner_index])
    return sum_uncalled * winner


def has_won(board, row_index, column_index):
    return sum(board[row_index]) == dimension or find_column_sum(board, column_index) == dimension


def find_column_sum(board, column_index):
    column_sum = 0
    for row_index in range(dimension):
        column_sum += board[row_index][column_index]
    return column_sum


def calculate_sum_uncalled(board_winner, board_winner_visited):
    sum_uncalled = 0
    for i in range(dimension):
        for j in range(dimension):
            if board_winner_visited[i][j] == 0:
                sum_uncalled += board_winner[i][j]
    print("Sum uncalled = ", sum_uncalled)
    return sum_uncalled


def day_4_2(path):
    numbers, boards, boards_visited = read_boards(path)
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
                        if has_won(boards_visited[board_index], row_index, n):
                            latest_winner = num
                            latest_board_winner_index = board_index
                            won_boards.add(latest_board_winner_index)
    print(numbers)
    print(boards)
    print(boards_visited)
    print("Last board to win #", latest_board_winner_index)

    sum_uncalled = calculate_sum_uncalled(boards[latest_board_winner_index], boards_visited[latest_board_winner_index])
    return sum_uncalled * latest_winner


def read_boards(path):
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

import copy

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]


def clean(m, n, board):
    for i in range(m - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            if board[i][j] == '0':
                continue
            x = i
            while x + 1 < m and board[x + 1][j] == '0':
                board[x + 1][j] = board[x][j]
                board[x][j] = '0'
                x += 1
    return board


def is_same(i, j, board, character):
    for k in range(1, 4):
        x = i + dx[k]
        y = j + dy[k]
        if board[x][y] != character:
            return False
    return True


def check(m, n, board):
    new_board = copy.deepcopy(board)
    character = ''
    anyone = False
    sumation = 0
    for i in range(m - 1):
        for j in range(n - 1):
            character = board[i][j]
            if character == '0':
                continue
            issame = is_same(i, j, board, character)
            if issame:
                anyone = True
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if new_board[x][y] != '0':
                        sumation += 1
                        new_board[x][y] = '0'

    return new_board, anyone, sumation


def solution(m, n, board):
    answer = 0

    my_board = [['' for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            my_board[i][j] = board[i][j]
    anyone = True
    sumation = 0
    while anyone:
        my_board, anyone, sumation = check(m, n, my_board)
        my_board = clean(m, n, my_board)
        answer += sumation

    return answer
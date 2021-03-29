

def resize(board):
    new_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[i + 1][j + 1] = board[i][j]

    return new_board


def solution(board):
    answer = -1

    new_board = resize(board)

    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if i == 0 or j == 0:
                continue

            if new_board[i][j] != 0:
                new_board[i][j] = min(new_board[i - 1][j], new_board[i][j - 1], new_board[i - 1][j - 1]) + 1
                if new_board[i][j] > answer:
                    answer = new_board[i][j]

    return answer ** 2
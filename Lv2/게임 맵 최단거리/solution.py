from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                maps[i][j] = 0
            else:
                maps[i][j] = -1

    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = 1

    while q:
        x, y, count = q.popleft()

        if x == n - 1 and y == m - 1:
            return count

        for i in range(4):
            tmp_x, tmp_y = x + dx[i], y + dy[i]
            if 0 <= tmp_x < n and 0 <= tmp_y < m and maps[tmp_x][tmp_y] == 0:
                maps[tmp_x][tmp_y] = count + 1
                q.append((tmp_x, tmp_y, count + 1))

    return -1
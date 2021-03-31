dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_direction(dir):
    if dir == 'U':
        direction = 0
    elif dir == 'R':
        direction = 1
    elif dir == 'D':
        direction = 2
    else:
        direction = 3
    return direction


def solution(dirs):
    answer = 0

    visited = set()
    # 위 : 0, 오른쪽 : 1, 아래 : 2, 왼쪽 3
    direction = 0
    x, y = 0, 0

    for i in range(len(dirs)):
        direction = find_direction(dirs[i])
        tmp_x, tmp_y = x + dx[direction], y + dy[direction]
        if -5 <= tmp_x <= 5 and -5 <= tmp_y <= 5:
            if (x, y, tmp_x, tmp_y) not in visited and (tmp_x, tmp_y, x, y) not in visited:
                visited.add((x, y, tmp_x, tmp_y))
                # print((x,y,tmp_x,tmp_y),i)
            x, y = tmp_x, tmp_y

    return len(visited)
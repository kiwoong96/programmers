import sys
input = sys.stdin.readline

N, M = map(int,input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))

dxy = [
    [[0,0],[1,0],[2,0],[2,1]],
    [[0,0],[1,0],[2,0],[2,-1]],
    [[0,0],[0,-1],[1,-1],[2,-1]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,0],[1,0],[1,-1],[1,-2]],
    [[0,0],[-1,0],[-1,-1],[-1,-2]],
    [[0,0],[-1,0],[-1,1],[-1,2]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,0],[1,0],[1,-1],[2,-1]],
    [[0,0],[0,1],[1,1],[1,2]],
    [[0,0],[0,1],[-1,1],[-1,2]],
    [[0,0],[1,0],[2,0],[1,1]],
    [[0,0],[1,0],[2,0],[1,-1]],
    [[0,0],[0,1],[0,2],[1,1]],
    [[0,0],[0,1],[0,2],[-1,1]],
    [[0,0],[0,1],[1,0],[1,1]],
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[0,2],[0,3]]]


def find(x,y):

    max_value = -1
    for k in dxy:
        result = 0
        for z in k:
            try:
                now_x = x+z[0]
                now_y = y+z[1]
                result += board[now_x][now_y]
            except:
                result = 0
                continue
        if max_value < result:
            max_value = result

    return max_value


result = -1

for i in range(N):
    for j in range(M):
        tmp = find(i,j)
        if result < tmp:
            result = tmp

print(result)

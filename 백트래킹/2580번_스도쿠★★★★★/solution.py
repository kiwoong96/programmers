import time
import sys
input = sys.stdin.readline

board = []
to_find = []
for i in range(9):
    tmp = list(map(int,input().split()))
    for k in range(len(tmp)):
        if tmp[k] == 0:
            to_find.append((i,k))
    board.append(tmp)

def print_board(board):
    for i in board:
        print(i)
    print()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y,value):
    #가로,세로
    for i in range(4):
        tmp_x, tmp_y = x+dx[i], y+dy[i]

        while 0<=tmp_x<9 and 0<=tmp_y<9:
            #print(tmp_x, tmp_y,board[tmp_x][tmp_y],value)
            #time.sleep(1)
            if board[tmp_x][tmp_y] == value:
                return False
            tmp_x +=dx[i]
            tmp_y +=dy[i]

    tmp_x,tmp_y = x//3*3,y//3*3

    for i in range(tmp_x,tmp_x+3):
        for j in range(tmp_y,tmp_y+3):
            if board[i][j] == value:
                return False



    return True

def DFS(count,data):
#    print("IMs")
    if count == len(to_find):
        return True

    for x,y in to_find:
        print(data[-3:-1])
#       print(3)
        if (x,y) in data:
            continue
#       print(5)
        for value in range(1,10):
            if check(x,y,value):
                board[x][y] = value
                data.append((x,y))
                if DFS(count+1,data):
                    return True
                data.remove((x,y))
                board[x][y] = 0
    return False

def solution():
    count = 0
    data = []
    x,y = to_find[0][0], to_find[0][1]
    DFS(count,data)

solution()
print_board(board)


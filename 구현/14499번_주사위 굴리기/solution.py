import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())

board = []


for i in range(N):
    board.append(list(map(int,input().split())))

move = list(map(int,input().split()))

dice = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

dxy = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]

for moving in move:
    if x+dxy[moving][0] < 0 or x+dxy[moving][0] >N-1 or y+dxy[moving][1] <0 or y+dxy[moving][1] > M-1:
        continue
    ##동쪽
    x,y = x+dxy[moving][0],y+dxy[moving][1]
    if moving == 1:
        dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[1][1],dice[1][2],dice[3][1],dice[1][0]
    ##서쪽
    elif moving == 2:
        dice[3][1], dice[1][0],dice[1][1],dice[1][2] = dice[1][2],dice[3][1],dice[1][0],dice[1][1]
    ##북쪽
    elif moving == 3:
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[3][1],dice[0][1],dice[1][1],dice[2][1]
    ##남쪽
    else:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1],dice[2][1],dice[3][1],dice[0][1]

    if board[x][y] == 0:
        board[x][y] = dice[1][1]
    else:
        dice[1][1] = board[x][y]
        board[x][y] = 0
    """
    print(x,y)
    for i in dice:
        print(i)
    """
    print(dice[3][1])
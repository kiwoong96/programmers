import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

board = []
max_height = 0
for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    if max_height < max(tmp):
        max_height = max(tmp)



dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def DFS(i,j,height):
    visited[i][j] = True

    for dt in dxy:
        tmp_i, tmp_j = i+dt[0], j+dt[1]
        if 0<=tmp_i<N and 0<=tmp_j<N:
            if visited[tmp_i][tmp_j] == False and board[tmp_i][tmp_j] >height:
                DFS(tmp_i,tmp_j,height)

max_value = -1
visited = [[0 for _ in range(N)]for _ in range(N)]
for height in range(0,max_height):

    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > height and visited[i][j] == False:
                DFS(i,j,height)
                count +=1

    if count>max_value:
        max_value = count
        #print(height,max_value)

print(max_value)



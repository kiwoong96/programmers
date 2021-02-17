import sys
input = sys.stdin.readline

T = int(input())

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def DFS(x,y):
    graph[x][y] =0

    for dt in dxy:
        tmp_x , tmp_y = x+dt[0],y+dt[1]
        if 0<=tmp_x<N and 0<=tmp_y<M:
            if graph[tmp_x][tmp_y] == 1:
                DFS(tmp_x,tmp_y)

for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    result = 0
    for i in range(K):
        y,x = map(int,input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                result +=1
                DFS(i,j)
    print(result)



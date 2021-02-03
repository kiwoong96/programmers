N,M,V = map(int,input().split())

arr = []
for i in range(M):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0])
visited = [0 for _ in range(N+1)]

def dfs(n):
    if visited[n]==0: #방문X
        visited[n]=1
        print(n,end = ' ')
        dfs()
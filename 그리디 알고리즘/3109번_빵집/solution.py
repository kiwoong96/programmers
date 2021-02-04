R,C = map(int,input().split())

map = []
visited = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    map.append(input())

dxy = [[-1,1],[0,1],[1,1]]

def dfs(x,y):
    if y == C-1:
        visited[x][y] = 1
        return 1
    if not(0<= x <R and 0<= y <C):
        return 0
    if map[x][y]=='.' and visited[x][y] == 0:
        for dt in dxy:
            dx = x+dt[0]
            dy = y+dt[1]
            visited[x][y] = dfs(dx,dy)
            if visited[x][y] == 1:
                break
    elif map[x][y] =='x' or visited[x][y] == 1:
        return 0
    print("DFS!")
    for i in range(R):
        print(visited[i])
    return visited[x][y]


for i in range(R):
    dfs(i,0)

result = 0
for i in range(R):
    result += visited[i][C-1]
print(result)
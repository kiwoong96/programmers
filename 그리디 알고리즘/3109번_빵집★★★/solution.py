"""R,C = map(int,input().split())

map = []
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    map.append(input())

dxy = [[-1,1],[0,1],[1,1]]

def dfs(x,y):
    if y == C-1:
        return True
    for dt in dxy:
        tmp_x, tmp_y = x+dt[0], y+dt[1]
        if 0 <= tmp_x <R and 0<= tmp_y<C and map[tmp_x][tmp_y]=='.' and visited[tmp_x][tmp_y] == False:
            visited[tmp_x][tmp_y] = True
            if dfs(tmp_x,tmp_y):
                return True

    return False


result = 0

for i in range(R):
    if dfs(i,0):
        result +=1

print(result)"""

R,C = map(int,input().split())

map = []
visited = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    map.append(input())

dxy = [[-1,1],[0,1],[1,1]]

def dfs(x,y):
    if y == C-1:
        return 1
    for dt in dxy:
        dx = x + dt[0]
        dy = y + dt[1]
        if 0<= dx <R and 0<= dy <C and map[dx][dy]=='.' and visited[dx][dy] == 0:
            visited[dx][dy] = 1
            if dfs(dx,dy):
                return 1
    return 0


for i in range(R):
    dfs(i,0)

result = 0
for i in range(R):
    result += visited[i][C-1]
print(result)
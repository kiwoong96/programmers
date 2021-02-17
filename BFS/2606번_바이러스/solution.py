import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]

def DFS(start):
    global count
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:

            DFS(i)

DFS(1)

print(sum(visited)-1)
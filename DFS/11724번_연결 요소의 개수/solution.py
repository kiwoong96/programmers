from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[]for _ in range(N+1)]

visited =  [False for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(start,visited):
    visited[start] = True

    for k in graph[start]:
        if visited[k] == False:
            print(start, k, visited)
            DFS(k,visited)

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        tmp = queue.popleft()
        for k in graph[tmp]:
            if visited[k] == False:
                queue.append(k)
                visited[k] = True


result = 0
for i in range(1,N+1):
    if visited[i] == False:
        BFS(i)
        result +=1
print(result)
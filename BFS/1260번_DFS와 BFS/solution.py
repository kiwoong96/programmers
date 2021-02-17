from _collections import deque
import sys
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[]for _ in range(N+1)]
for i in range(M):
    tmp = list(map(int,input().split()))
    a,b = tmp[0],tmp[1]
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

visited = [False for _ in range(N+1)]

result_DFS = []
def DFS(start,result):
    result.append(start)
    visited[start] = True
    for k in graph[start]:
        if visited[k] ==False:
            DFS(k,result)

def DFS2(start):
    visited = []
    stack = [start]

    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            stack += reversed(graph[tmp])
    return visited

def BFS(start):
    queue = deque()
    queue.append(start)
    visited = []

    while queue:
        tmp = queue.popleft()
        if tmp not in visited:
            visited.append(tmp)
            for i in graph[tmp]:
                if i not in visited: queue.append(i)
    return visited
"""
result = DFS2(V)
print(result)
"""

result_BFS = BFS(V)
DFS(V,result_DFS)


for i in result_DFS:
    print(i, end =' ')
print()
for i in result_BFS:
    print(i,end = ' ')


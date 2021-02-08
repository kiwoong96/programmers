import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

M,N = map(int,input().split())
dxy = [[1,0],[-1,0],[0,1],[0,-1]]
board = [input().rstrip() for _ in range(N)]
distance = [[INF for _ in range(M)] for _ in range(N)]



#print(board)


def dijkstra(start_x,start_y):
    q = []
    heapq.heappush(q,(0,start_x,start_y))
    distance[start_x][start_y] = 0

    while q:
        dist,x,y = heapq.heappop(q)
        if x==N-1 and y==M-1:
            pass
        if distance[x][y] < dist:
            continue

        for i in dxy:
            to_x,to_y = x + i[0], y+i[1]
            if 0<= to_x < N and 0<= to_y < M:
                if board[to_x][to_y] == '1':
                    if distance[to_x][to_y] > distance[x][y] + 1:
                        distance[to_x][to_y] = distance[x][y] + 1
                        heapq.heappush(q, (distance[x][y] + 1, to_x, to_y))
                        #print("to_x :", to_x, ", to_y : ", to_y, "distance[to_x][to_y] : ", distance[to_x][to_y])
                        #print(q)
                else:
                    if distance[to_x][to_y] > distance[x][y] + 1:
                        distance[to_x][to_y] = distance[x][y]
                        heapq.heappush(q,(distance[x][y],to_x,to_y))
                        #print("to_x :", to_x, ", to_y : ", to_y, "distance[to_x][to_y] : ", distance[to_x][to_y])

dijkstra(0,0)
print(distance[N-1][M-1])
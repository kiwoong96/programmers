"""
1st
"""
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

#Direction
# Right : 0
# Down  : 1
# Left  : 2
# Up    : 3
# NoDir : 4
def calc(tmpDir,newDir,price):
    if tmpDir == 4 or tmpDir == newDir:
        return price + 100
    if (tmpDir == 0 or tmpDir == 2) and (newDir == 1 or newDir == 3):
        return price + 600
    if (tmpDir == 1 or tmpDir == 3) and (newDir == 0 or newDir == 2):
        return price + 600
    
    
def solution(board):
    def dijkstra(board,dir):
        flag = -1
        if dir == 0 and board[0][1] == 0:
            board[0][1] = 1
            flag = 0
        elif dir == 1 and board[1][0] == 0:
            board[1][0] = 1
            flag = 1

        answer = []
        N = len(board)
        dp = [[1e9 for _ in range(N)] for _ in range(N)]
        q = deque()
        q.append((0,0,4,0)) 
        dp[0][0] = 0    
        count = 0
        while q:
            x,y,dir,price = q.popleft()
            for i in range(4):
                tmpX,tmpY = x+dx[i], y+dy[i]
                tmpPrice = calc(dir,i,price)
                if abs(dir - i) == 2:
                    continue
                #방문 가능한 경우
                if 0<=tmpX<=N-1 and 0<=tmpY<=N-1 and board[tmpX][tmpY] != 1:
                    #건설비가 더 작은 경우
                    if tmpPrice <= dp[tmpX][tmpY]:
                        dp[tmpX][tmpY] = tmpPrice
                        q.append((tmpX,tmpY,i,tmpPrice))
        if flag == 0:
            board[0][1] = 0
        elif flag == 1:
            board[1][0] = 0
        return dp[N-1][N-1]
    
    return min(dijkstra(board,0),dijkstra(board,1))


"""
2nd
"""


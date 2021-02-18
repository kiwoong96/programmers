import sys
input = sys.stdin.readline


R, C = map(int,input().split())
board = []
for i in range(R):
    board.append(input())


dxy = [[0,1],[0,-1],[1,0],[-1,0]]
result = [False for _ in range(26)]
cnt = 1
max_cnt = 0
def DFS(x,y,cnt,result):
    global max_cnt

    if max_cnt < cnt: max_cnt = cnt
    result[ord(board[x][y])-65] = True

    #print(result)
    for dt in dxy:
        tmp_x, tmp_y = x+dt[0],y+dt[1]
        if 0<=tmp_x<R and 0<=tmp_y<C:
            if result[ord(board[tmp_x][tmp_y])-65] == False:
                #print(tmp_x, tmp_y, result)

                DFS(tmp_x,tmp_y,cnt+1,result)
                result[ord(board[tmp_x][tmp_y])-65] = False
                #print("End : ", tmp_x, tmp_y, result  )


DFS(0,0,cnt,result)

print(max_cnt)



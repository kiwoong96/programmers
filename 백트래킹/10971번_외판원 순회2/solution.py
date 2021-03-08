import copy
import sys
input = sys.stdin.readline

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

result = []

def DFS(count,now_result,data):
    global result
    #print("count : ", count)
    if count == N:
        if board[data[-1]][data[0]] != 0:
            tmp_result = copy.deepcopy(now_result)
            tmp_result += board[data[-1]][data[0]]
            result.append(tmp_result)
            return
        else:
            return
    else:
        for i in range(N):
            if i in data or board[data[-1]][i] == 0:
                continue
            tmp_result = copy.deepcopy(now_result)
            tmp_result += board[data[-1]][i]

            tmp_data = copy.deepcopy(data)
            tmp_data.append(i)
            #print("i : ", i, "data : ", tmp_data,"이동")
            DFS(count+1,tmp_result,tmp_data)





def solution():
    global result
    count = 1
    now_result = 0
    data = []
    for idx in range(N):
        data.append(idx)
        DFS(count,now_result,data)

solution()
print(min(result))




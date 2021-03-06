from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dN = [-1,1,2]

def solution(N,K):
    visited = [1e9 for _ in range(100001)]
    q = deque()
    count = 0
    q.append((count,N))
    result = 0
    min_val = 1e9
    while q:

        count, N = q.popleft()

        if count > min_val :
            break

        if N == K:
            min_val = count
            if min_val == count:
                result +=1
            continue
        for i in range(len(dN)):
            if i == 2:
                now_N = N*dN[i]
            else:
                now_N = N+dN[i]

            if 0<=now_N<=100000 and visited[now_N] >= count + 1:
                q.append((count+1,now_N))
                visited[now_N] = count+1


    return min_val,result


min_val ,result = solution(N,K)
print(min_val)

print(result)

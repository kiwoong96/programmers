from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dN = [-1,1,2]

def solution(N,K):
    dp = [1e9 for _ in range(200001)]

    q = deque()
    cnt = 0
    q.append((N,cnt))
    while q:
        N,cnt = q.popleft()

        if N == K:
            break

        for i in range(3):
            if i == 2:
                now_N = N*dN[i]
            else:
                now_N = N+dN[i]

            if 0<=now_N<=200000 and dp[now_N] > cnt + 1:
                q.append((now_N,cnt+1))
                dp[now_N] = cnt + 1



    return cnt

result = solution(N,K)
print(result)
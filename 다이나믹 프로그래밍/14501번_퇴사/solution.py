##내 풀이

"""
N = int(input())

arr = [[0 for _ in range(2)] for _ in range(N+1)]

for i in range(1,N+1):
    arr[i] = list(map(int,input().split()))

d = [0 for i in range(N+1)]

for i in range(1,N+1):
    if arr[i][0] + i <= (N+1):
        d[i] = arr[i][1]



for i in range(2,N+1):
    if (i + arr[i][0]) > (N+1):
        #print("Stop")
        continue
    for j in range(1, i):
        if (j+arr[j][0]) <= i:
            d[i] = max(d[i], d[j] + arr[i][1])
            #print("i : ", i ,", j : ", j ," d[i] : ",d[i])

print(max(d))
"""

##정석 풀이

N = int(input())

T = [0 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
for i in range(1,N+1):
    x,y = map(int,input().split())
    T[i] = x
    P[i] = y
    dp[i] = y

dp.append(0)

for i in range(N, 0, -1):
    if T[i] + i > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[i+ T[i]] + P[i])

print(dp[1])

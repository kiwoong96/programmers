N = int(input())

arr =  list(map(int,input().split()))
arr.insert(0,0)

dp = [[1 for _ in range(1001)] for _ in range(2)]

dp[0][1] = 1
dp[1][N] = 1
for i in range(1,N+1):
    for j in range(1,i):
        if arr[i] > arr[j]:
            dp[0][i] = max(dp[0][j] + 1, dp[0][i])

for i in range(N,0,-1):
    for j in range(N,i,-1):
        if arr[i] > arr[j]:
            #print(i,j)
            dp[1][i] = max(dp[1][j] + 1,dp[1][i])

"""print(dp[0])
print(dp[1])"""
rslt = -1

for i in range(N+1):
    if (dp[0][i] + dp[1][i] - 1) > rslt:
        rslt = (dp[0][i] + dp[1][i] -1)

print(rslt)
N = int(input())


arr = list(map(int,input().split()))
arr.insert(0,0)

dp = [0 for _ in range(N+1)]

dp[1] = arr[1]
dp[2] = max(arr[2], arr[1]*2)


for i in range(3, N+1):
    for j in range(0, i):
        dp[i] = max(dp[j] +arr[i-j],dp[i])

print(max(dp))
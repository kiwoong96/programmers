N = int(input())

arr = list(map(int,input().split()))
arr.insert(0,0)

dp = [1 for _ in range(N+1)]

for i in range(2,N+1):
    for j in range(1,i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

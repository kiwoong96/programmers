N = int(input())

arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [0 for _ in range(1001)]


for i in range(1,N+1):
    dp[i] = arr[i]
    for j in range(1,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+arr[i],dp[i])
        elif arr[i] < arr[j] and dp[i] == 0:
            dp[i] = 1
print(max(dp))
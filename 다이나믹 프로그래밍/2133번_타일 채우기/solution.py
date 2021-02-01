N = int(input())

dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(3,N+1):
    dp[i] += dp[i-2]*3
    tmp = i-4
    while tmp>=0:
        if tmp == 0:
            dp[i] += 2
        else:
            dp[i] += dp[tmp]*2
        tmp -= 2

print(dp[N])
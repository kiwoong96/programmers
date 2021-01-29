N = int(input())

dp = [i for i in range(100001)]



for i in range(2,N+1):
    for j in range(1,i):
        #print("i : ", i, ",j : ", j,", i/j : ",i/j)
        if j*j > i:
            break
        else:
            dp[i] = min(dp[i],dp[i-j*j]+1)

print(dp[N])

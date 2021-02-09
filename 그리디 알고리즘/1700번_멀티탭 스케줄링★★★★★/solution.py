N, K = map(int,input().split())

arr = list(map(int,input().split()))

dp = [0 for _ in range(101)]

count = 0

result = 0
for i in range(0,K):
    if count < N:
        if dp[arr[i]] == 1:
            continue
        else:
            dp[arr[i]] = 1
            count += 1
    else:
        tmp = [0 for _ in range(K + 1)]
        if dp[arr[i]] == 0:
            for j in range(i + 1, K):
                if dp[arr[j]] == 1:
                    tmp[arr[j]] = 1
                else:
                    continue
                if sum(tmp) == sum(dp) - 1:
                    break
            for k in range(K+1):
                if dp[k] != tmp[k]:
                    dp[k] = 0
                    dp[arr[i]] = 1
                    result += 1
                    break
        else:
            continue
    #print(dp)
print(result)

T = int(input())

dp = [0,1]
i = 2

while True:
    dp.append(dp[i-2] + dp[i-1])
    if dp[i]>= 1000000000:
        break
    i += 1
#print(dp)


for i in range(T):
    N = int(input())
    list = []
    for j in range(len(dp)-1,-1,-1):
        if dp[j] == 0: break
        if dp[j] <= N:
            list.append(dp[j])
            N -= dp[j]
        else:
            continue
    list.sort()
    for data in list:
        if list[-1] != data:
            print(data,end=' ')
        else:
            print(data)
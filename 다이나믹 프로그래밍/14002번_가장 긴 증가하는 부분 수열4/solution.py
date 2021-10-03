import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

dp = [[1,[str(arr[i])]] for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1][:]
                dp[i][1].append(str(arr[i]))
maxVal = -1
maxIdx = -1
for i in range(N):
    if maxVal < dp[i][0]:
        maxVal = dp[i][0]
        maxIdx = i
if maxIdx == -1:
    print(0)
    print(arr[0])
else:
    print(maxVal)
    print(' '.join(dp[maxIdx][1]))


"""
6
10 20 10 30 20 50
"""
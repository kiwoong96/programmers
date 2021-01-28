arr = []

for i in range(2):
    arr.append(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(len(arr[0])):
    for j in range(len(arr[1])):
        if arr[0][i] == arr[1][j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1] ,dp[i+1][j])



print(dp[len(arr[0])][len(arr[1])])
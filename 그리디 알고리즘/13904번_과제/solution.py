N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [0 for _ in range(1000)]

arr.sort(key = lambda x : -x[1])

print(arr)
for i in range(N):
    j = arr[i][0]-1
    while j>=0:
        if dp[j] == 0:
            dp[j] = arr[i][1]
            break
        else:
            j -= 1
    print(dp)
print(sum(dp[0:1000]))
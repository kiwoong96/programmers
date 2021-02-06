N, C = map(int,input().split())

M = int(input())

arr = []
for i in range(M):
    arr.append(list(map(int,input().split())))


arr.sort(key = lambda x:x[0])


dp = [0 for _ in range(M+1)]

weight = 0
pos = 1
before = 0
j = 0
#print(arr)
for i in range(M):
    if before != arr[i][0]:
        #print("Before" , before, arr[i][0])
        for j in range(before,arr[i][0]+1):
            weight -= dp[j]
            ##dp[j] = 0
        before = arr[i][0]
    if weight < C:
        #print(C-weight,arr[i][2],weight)

        dp[arr[i][1]] += min(C-weight, arr[i][2])
        weight += min(C - weight, arr[i][2])
    #print(dp,i)

print(sum(dp))



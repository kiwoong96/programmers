N, C = map(int,input().split())

M = int(input())

arr = []
for i in range(M):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:(x[1], x[0]))

village = [C for _ in range(N+1)]

result = 0

for i in range(len(arr)):
    start, end = arr[i][0], arr[i][1]
    bags = arr[i][2]
    max_value = min(village[start:end])

    if max_value == 0:
        continue

    if bags <= max_value:
        for j in range(start,end):
            village[j] -= bags
        result += bags
    else:
        for j in range(start,end):
            village[j] -= max_value
        result += max_value

print(result)




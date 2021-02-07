N, M = map(int,input().split())

J = int(input())

arr = []

for i in range(J):
    arr.append(int(input()))

start = 1
end = M

result = 0
for i in range(J):
    if arr[i] > end:
        result += arr[i] - end
        end = arr[i]
        start = end - M + 1
    elif arr[i] < start:
        result += start - arr[i]
        start = arr[i]
        end = start + M - 1

print(result)

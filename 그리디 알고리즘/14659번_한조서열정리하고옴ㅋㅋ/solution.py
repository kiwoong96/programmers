N = int(input())

arr = list(map(int,input().split()))

max_val = -1
cnt = 0
now = 0
for data in arr:
    if data<=now:
        cnt += 1
    else:
        now = data
        cnt = 0
    max_val = max(cnt,max_val)


print(max_val)
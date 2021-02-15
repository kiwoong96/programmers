import sys
input = sys.stdin.readline


S = input().strip('\n')

count = [0 for _ in range(10)]

for i in S:
    tmp = int(i)
    if tmp == 6 or tmp == 9:
        if count[6] < count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[tmp] += 1

print(max(count))
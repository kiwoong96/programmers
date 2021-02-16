"""import sys
input = sys.stdin.readline

N = int(input())

arr = []
count = [0 for _ in range(8001)]
for i in range(N):
    tmp = int(input())
    arr.append(tmp)
    count[tmp+4000] += 1


print(int(round(sum(arr)/len(arr),0)))
arr.sort()
print(arr[len(arr)//2])


if count.count(max(count))>=2:
    cnt = 0
    for i in range(len(count)):
        if count[i] == max(count):
            cnt+=1
            if cnt == 2:
                print(i-4000)
                break
else:
    print(count.index(max(count))-4000)


print(arr[-1] - arr[0])

"""

#다른풀이 최빈값 구하

from collections import Counter

a = [-1,-2,-4,-3,-2,-1]
mode_dict = Counter(a)  ##개수를 세주는기 Collection.counter 형태로 변환
print(type(mode_dict))

mode = mode_dict.most_common() ##Counter형태를 list형태로 변환

print(mode)
print(type(mode))
if len(a) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
import sys

S = list(sys.stdin.readline().rstrip("\n").split())

language = ''
for i in range(len(S)):
    language +=S[i]

Find = "UCPC"

j = 0
result = 0

for i in range(len(language)):
    if language[i] ==Find[j]:
        result += 1
        j += 1
    if result == 4:
        break
if result == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
A,B = map(int,input().split())

result = 0

while True:
    if A==B:
        result += 1
        break
    if (B%2 != 0 and B%10 !=1) or B<A:
        result = -1
        break
    else:
        if B % 10 == 1:
            B = B // 10
            result += 1
        elif B % 2 == 0:
            B = B // 2
            result += 1

print(result)
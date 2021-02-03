N = int(input())

S = input()

count = [0,0]

##SLLLLSSLL
tmp = 0

for i in range(len(S)):
    if S[i] == 'S':
        count[0] +=1
    elif S[i] == 'L':
        if tmp == 0:
            count[1] +=1
            tmp += 1
        else:
            tmp = 0

if count[1] !=0:
    result = count[0] + count[1] + 1
else:
    result = count[0]
print(result)
S = input()

count = [0,0]
before = S[0]
count[int(before)] +=1
for i in range(1,len(S)):
    tmp = S[i]
    if before == tmp:
        continue
    else:
        if before == '1':
            #print("1->0 : ",i)
            count[0] += 1
        elif before == '0':
            #print("0->1 : ",i)
            count[1] += 1
        before = tmp

#print(count)
print(min(count))
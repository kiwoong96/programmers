N = int(input())

distance = list(map(int,input().split()))
vertex = list(map(int,input().split()))

tmp_oil = vertex[0]
result = 0

for i in range(len(vertex)-1):
    if tmp_oil <= vertex[i+1]:
        result += tmp_oil*distance[i]
    else:
        result += tmp_oil*distance[i]
        tmp_oil = vertex[i+1]

print(result)
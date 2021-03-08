##라이브러리 활용

"""
from itertools import permutations
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

data_N = [i+1 for i in range(N)]
data =list(permutations(data_N,M))
for now in data:
    for k in now:
        print(k, end=' ')
    print()
"""
import sys
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
result = []

def DFS(count,a1,str):
    if count == M+1:
        result.append(a1)
        return
    for i in range(1,N+1):
        if i in a1:
            continue
        tmp_a1 = copy.deepcopy(a1)
        tmp_a1.append(i)
        DFS(count+1,tmp_a1,str)





def solution():
    a1 = []
    count = 1
    str = ''
    DFS(count,a1,str)

solution()
for i in result:
    for now in i:
        print(now, end= ' ')
    print()
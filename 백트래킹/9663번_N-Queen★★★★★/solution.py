import sys
input = sys.stdin.readline


N = int(input())
count = 0

def DFS(x,a1,a2,a3):
    global count

    if x == N+1:
        count += 1
        return

    for i in range(1,N+1):
        if i in a1 or x+i in a2 or x-i in a3:
            continue
        a1.add(i)
        a2.add(x+i)
        a3.add(x-i)
        DFS(x+1,a1,a2,a3)
        a1.remove(i)
        a2.remove(x+i)
        a3.remove(x-i)



def solution(N):
    #a1 = 세로 a2 = 왼쪽 대각선 a3 = 오른쪽 대각선
    a1 ,a2, a3 = set(),set(),set()
    DFS(1,a1,a2,a3)


solution(N)
print(count)







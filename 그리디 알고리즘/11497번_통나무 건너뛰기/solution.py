T = int(input())



for i in range(T):
    N = int(input())
    arr = []
    arr = list(map(int,input().split()))
    arr.sort(reverse = True)
    max_val = -1
    for j in range(2,N):
        if abs(arr[j]-arr[j-2]) > max_val:
            max_val = abs(arr[j]- arr[j-2])
    print(max_val)

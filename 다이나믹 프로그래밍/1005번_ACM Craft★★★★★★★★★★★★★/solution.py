T = int(input())




for j in range(T):

    N, K = map(int, input().split())

    direction = []
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    price = list(map(int, input().split()))



    for i in range(K):
        tmp = list(map(int, input().split()))
        x = tmp[0]
        y = tmp[1]
        print(dp)
        dp[x][y] = price[x-1]
    W = int(input())



    print(dp)


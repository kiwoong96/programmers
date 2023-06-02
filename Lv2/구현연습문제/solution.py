#.1 마름모의 합
# 1 2 6 1 7 
# 1 6 7 2 1 
# 6 7 7 5 1
# 0 1 3 2 6
# 1 2 8 2 1
# input = [[1,2,6,1,7],[1,6,7,2,1],[6,7,7,5,1],[0,1,3,2,6],[1,2,8,2,1]]
# n = 5(홀수)

def solution1(input, n):
    answer = 0
    for i in range(n):
        if i <= n//2:
            start, end = n//2 - i, n//2 + i
        else: 
            start, end = i - n//2 , n - 1 - (i - n//2)
            
        answer += sum(input[i][start:end+1])
        
    return answer

input = [[1,2,6,1,7],[1,6,7,2,1],[6,7,7,5,1],[0,1,3,2,6],[1,2,8,2,1]]
n = 5

#print(solution1(input, n))


#2. 뱀
# 1  2  3  4  5
# 16 17 18 19 6 
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# n = 5
def solution2(n):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    #방향
    # 0:오른쪽
    # 1:아래쪽
    # 2:왼쪽
    # 3:위쪽
    dir = 0 
    
    #방향전환횟수
    cnt = 0
    #진행칸수
    count = 2
    #뱀의머리
    x,y = 0,0
    visited[0][0] = 1
    while True:
        n_x, n_y = x+dx[dir], y+dy[dir]
        #방문하지않았을 경우
        if n_x >= 0 and n_x < n and n_y >= 0 and n_y < n and visited[n_x][n_y] == -1:
            visited[n_x][n_y] = count
            count += 1
            x,y = n_x,n_y
            cnt = 0
        else:
            cnt += 1
            dir = (dir + 1) % 4
        if cnt == 4: 
            break
    for v in visited:
        print(v)
    return

#solution2(n)

def solution3(n):
    dp = [i for i in range(n+1)]
    #1,4,6
    coins = [1,4,6]
    for coin in coins:
        for i in range(coin, n+1):
            if i % coin == 0:
                dp[i] = i//coin
            else:
                dp[i] = min(dp[i-coin]+dp[coin], dp[i])
    return dp[-1]

print(solution3(100))
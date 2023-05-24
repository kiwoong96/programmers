def solution(scores):
    answer = -1
    new_scores = []
    x,y = scores[0]
    scores.sort(key=lambda x : (x[0],x[1]),reverse=True)
    
    dp = [[-1 for _ in range(2)] for _ in range(100002)]
    for i in range(len(scores)):
        if dp[scores[i][0]][1] == -1:
            dp[scores[i][0]][0] = scores[i][0]
            dp[scores[i][0]][1] = scores[i][1]
        else:
            continue
    for i in range(100000,-1,-1):
        if dp[i][0] == -1:
            dp[i][0] = dp[i+1][0]
            dp[i][1] = dp[i+1][1]
        else:
            dp[i][1] = max(dp[i+1][1], dp[i][1])
    
    for i in range(len(scores)):
        if scores[i][1] < dp[scores[i][0]+1][1]:
            continue
        else:
            new_scores.append([scores[i][0],scores[i][1]])
    
    new_scores.sort(key=lambda x : x[0]+x[1], reverse=True)
    for i in range(len(new_scores)):
        if x == new_scores[i][0] and y == new_scores[i][1]:
            answer = i+1
            break
            
    return answer
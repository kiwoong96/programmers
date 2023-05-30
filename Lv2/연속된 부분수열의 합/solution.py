#기본 풀이
def solution(sequence, k):
    answer = []
    start, end = 0, 0
    tmp_sum = 0
    while True:
        if tmp_sum < k:
            end += 1
            if end >= len(sequence):
                break
            tmp_sum += sequence[end]
        else:
            tmp_sum -= sequence[start]
            start += 1
            if start >= len(sequence):
                break
            
        if tmp_sum == k:
            answer.append([start,end])
    answer.sort(key=lambda x:(x[1]-x[0],x[0]), reverse=True)
    return answer[-1]


#DP를 이용하여 풀이
def solution(sequence, k):
    answer = []
    dp = [0 for _ in range(len(sequence)+1)]
    dp[1] = sequence[0]
    for i in range(1, len(sequence)):
        dp[i+1] = dp[i] + sequence[i]   #dp : 0 0 1 2 3 4 5 6
                                        #seq:   0 1 2 3 4 5 6
    start, end = 0, 1
    while start < end and end < len(sequence)+1:
        now = dp[end]-dp[start]
        if now < k:
            end += 1
        elif now == k:
            answer.append([start,end-1])
            end += 1
        else:
            start += 1
    answer.sort(key=lambda x:(x[1]-x[0],x[0]), reverse=True)
    
    return answer[-1]

    


sequence = [1, 1, 1, 2, 3, 4, 5]	
k = 5
print(solution(sequence,k))
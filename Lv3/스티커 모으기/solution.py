def solution(sticker):
    answer = 0
    dp0 = [0 for _ in range(len(sticker))]
    dp1 = [0 for _ in range(len(sticker))]
    
    #0번부터 시작
    for i in range(len(sticker)):
        if i == 0:
            dp0[i] = sticker[i]
        elif i == 1:
            dp0[i] = max(dp0[i-1], sticker[i])
        elif i == len(sticker)-1 :
            dp0[i] = max(dp0[i-1], dp0[i-2])
        else:
            dp0[i] = max(dp0[i-1], dp0[i-2] + sticker[i])
    
    #1번부터 시작        
    for i in range(len(sticker)):
        if i == 0:
            pass
        elif i == 1:
            dp1[i] = sticker[i]
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    answer = max(max(dp0),max(dp1))
    
    
    return answer

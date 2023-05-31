from itertools import permutations

def solution(picks, minerals):
    answer = 1e9
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    pickList = []
    for i in range(3):
        for _ in range(picks[i]):
            pickList.append(i)
    
    pickComb = list(permutations(pickList,min(10,len(pickList))))
    print(pickComb)
    cnt = 0
    tmpTired = 0
    for k in range(len(pickComb)):
        pickIdx = 0
        for i in range(min(len(minerals),len(pickComb[k])*5)):
            if minerals[i] == "diamond":    #다이아몬드
                tmpTired += tired[pickComb[k][pickIdx]][0]
            elif minerals[i] == 'iron':     #강철
                tmpTired += tired[pickComb[k][pickIdx]][1]
            else: #돌
                tmpTired += tired[pickComb[k][pickIdx]][2]
            cnt += 1
            
            if cnt == 5:
                pickIdx += 1
                cnt = 0
        answer = min(answer,tmpTired)
    return answer


minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
picks = [0, 1, 1]
solution(picks, minerals)
from copy import deepcopy

def solution(sequence):
    answer = 0
    seq_1 = deepcopy(sequence)
    seq_2 = deepcopy(sequence)
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            seq_1[i] *= -1
        else:
            seq_2[i] *= -1
             
    dp_seq = [[0 for _ in range(len(sequence)+ 1)] for _ in range(2)]
    dp_seq[0][0] = seq_1[0]
    dp_seq[1][0] = seq_2[0]
    
    for i in range(1,len(sequence)):
        dp_seq[0][i] = max(0,dp_seq[0][i-1]) + seq_1[i]
        dp_seq[1][i] = max(0,dp_seq[1][i-1]) + seq_2[i]
        
    answer = max(max(dp_seq[0]),max(dp_seq[1]))
    
    return answer
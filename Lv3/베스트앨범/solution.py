from collections import defaultdict

def solution(genres, plays):
    answer = []
    song_dict = defaultdict(list)
    song_cnt_dict = defaultdict(int)
    for i in range(len(genres)):
        song_cnt_dict[genres[i]] += plays[i]
        song_dict[genres[i]].append((i,plays[i]))
    
    for (k,v) in sorted(song_cnt_dict.items(),key=lambda x:x[1], reverse = True):
        for (i,p) in sorted(song_dict[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer
        
    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres,plays)


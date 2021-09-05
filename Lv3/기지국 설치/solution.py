def solution(n, stations, w):
    answer = 0
    data = []
    
    if stations[0]-w-1 > 0:
        data.append(stations[0]-w-1)
    for i in range(len(stations)-1):
        if (stations[i+1]-w) - (stations[i]+w) - 1> 0:
            data.append((stations[i+1]-w) - (stations[i]+w) - 1)
    if n-(stations[-1]+w) > 0:
        data.append(n - (stations[-1]+w))
    
    print(data)
    for length in data:
        if length//(w*2+1) == 0:
            answer += 1
        else:
            answer += length//(w*2+1)
            if length%(w*2+1) == 0:
                pass
            else:
                answer += 1

    return answer
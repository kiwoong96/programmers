import math

def calDist(key,nowX,nowY):
    keyX, keyY = 0,0
    if key == 0:
        keyX,keyY = 3,1
    elif key <= 3:
        keyX,keyY = 0, key-1
    elif key <= 6:
        keyX,keyY = 1, key%4
    else:
        keyX,keyY = 2, key%7
    
    return abs(keyX-nowX) + abs(keyY-nowY), keyX,keyY

def solution(numbers, hand):
    answer = ''
    
    Lx,Ly = 3,0
    Rx,Ry = 3,2
    for key in numbers:
        if key == 1 or key == 4 or key == 7:   
            Lx = key//3
            Ly = 0
            answer += "L"
        elif key == 3 or key == 6 or key == 9:
            Rx = (key-1)//3 
            Ry = 2
            answer += "R"
        else:
            distL,keyX,keyY = calDist(key,Lx,Ly)
            distR,keyX,keyY = calDist(key,Rx,Ry)

            if distL < distR:
                Lx,Ly = keyX,keyY
                answer += "L"
            elif distL > distR:
                Rx,Ry = keyX,keyY
                answer += "R"
            else:
                if hand == "right":
                    Rx,Ry = keyX,keyY
                    answer += "R"
                else:
                    Lx,Ly = keyX,keyY
                    answer += "L"
                    
    return answer
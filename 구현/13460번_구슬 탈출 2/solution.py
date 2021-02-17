import sys
input = sys.stdin.readline

N,M = map(int,input().split())

board = []
red_x,red_y,blue_x,blue_y = 0,0,0,0

for i in range(N):
    tmp = input().strip('\n')
    for j in range(len(tmp)):
        if tmp[j] == 'R':
            red_x,red_y = i,j
        elif tmp[j] == 'B':
            blue_x,blue_y = i,j

cnt = 0
dx = [[0,1],[0,-1],[1,0],[-1,0]]






"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""
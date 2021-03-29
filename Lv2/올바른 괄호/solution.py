# from collections import deque

def solution(s):
    answer = True
    stack = []

    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True
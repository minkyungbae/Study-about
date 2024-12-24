def solution(sides):
    answer = 0
    
    if max(sides) < sum(sides) - max(sides):
        return 1
    else:
        return 2
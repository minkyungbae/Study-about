def solution(a, b):
    # 홀수이냐 아니냐에 따라 계산 방식이 달라짐
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    
    elif a % 2 == 1 or b % 2 == 1:
        return ((a+b)*2)
    
    else:
        return abs(a-b)

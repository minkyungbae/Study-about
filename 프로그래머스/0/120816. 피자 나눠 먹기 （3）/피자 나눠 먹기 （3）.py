def solution(slice, n):
    1 < slice < 11
    
    if n % slice != 0:
        answer = 1
    else:
        answer = 0
    
    return answer + (n // slice)

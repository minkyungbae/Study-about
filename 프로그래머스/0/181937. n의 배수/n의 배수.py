def solution(num, n):
    answer = 0
    
    for i in range(1, num+1):
        if i % n ==0:
            answer = 1
        else:
            answer = 0
            
    return answer
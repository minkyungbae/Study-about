def solution(order):
    answer = 0
    clapping = ["3", "6", "9"]
    
    for i in str(order):
        if i in clapping:
            answer += 1
            
    return answer
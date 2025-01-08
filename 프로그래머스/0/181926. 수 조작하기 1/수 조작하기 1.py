def solution(n, control):
    answer = n
    control_num = {
        "w":+1, "s":-1, "d": +10, "a":-10
    }
    
    for i in control:
        answer += control_num[i]
        
    return answer

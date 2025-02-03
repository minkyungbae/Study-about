def solution(start_num, end_num):
    answer = []
    
    for time in range(start_num,end_num-1, -1):
        answer.append(time)
    return answer
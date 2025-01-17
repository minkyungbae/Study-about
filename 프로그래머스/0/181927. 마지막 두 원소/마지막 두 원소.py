def solution(num_list):
    answer = num_list
    
    if num_list[-1] > num_list[-2]:     # 뒤에서 두 번째 값이 마지막 값보다 작을 때
        answer.append(num_list[-1] - num_list[-2])
    
    else:
        answer.append(num_list[-1]*2)
        
    return answer
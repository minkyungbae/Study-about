def solution(num_list):
    answer = [0,0]
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
            
        if num % 2 != 0:
            answer[1] += 1
    return answer
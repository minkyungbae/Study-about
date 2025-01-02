def solution(num_list):
    answer = 0
    multiply = 1
    add = 0
    
    for i in range(len(num_list)):
        multiply *= num_list[i]
        add += num_list[i]
        
        if multiply < add**2:
            answer = 1
        else:
            answer = 0
           
    return answer

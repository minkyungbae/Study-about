def solution(sides):
    answer = 0
    max_num = max(sides)
    min_num = min(sides)
    sum_num = sum(sides)
    
    #가장 긴 변이 sides에 있을 경우
    for i in range(1, max_num+1):
        if i+min_num > max_num: 
            answer += 1
            
    #가장 긴 변이 새로운 변일 경우
    for i in range(max_num+1, sum_num):
        answer +=1
    
    return answer
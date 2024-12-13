def solution(array, height):
    answer = []
    
    for arrs in array:
        if height < arrs:
            answer.append(arrs)
            
    return len(answer)
def solution(todo_list, finished):
    answer = []
    
    for idx, val in enumerate(finished):
        print(val) # True는 자동으로 나오는 걸 확인함
        
        if val == False:
            answer.append(todo_list[idx])
            
    return answer
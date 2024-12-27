def solution(num, k):
    answer = -1  # 시작을 2로 설정
    str_num = str(num)
    
    for i in str_num:
        if i == str(k):
            answer = str_num.index(i)+1
        
    return answer
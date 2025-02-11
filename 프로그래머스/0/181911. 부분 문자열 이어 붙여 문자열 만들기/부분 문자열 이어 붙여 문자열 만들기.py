def solution(my_strings, parts):
    answer = ''
    
    for idx, val in enumerate(parts):
        print(idx, val) # 2차원 리스트의  인덱스 번호에 접근함
        # my_strings는 리스트에 있는 문자열이라서 idx,
        # 문자열 이어붙이기 위해 [][] 형식으로 함
        # val[]:val[]+1은 슬라이싱 범위, 마지막 범위는 포함되지 않으니까 +1 해줌
        answer += my_strings[idx][val[0]:val[1]+1]
        
    return answer
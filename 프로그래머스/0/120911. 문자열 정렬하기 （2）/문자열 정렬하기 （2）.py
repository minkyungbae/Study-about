def solution(my_string):
    answer = ''
    
    alphabet_lower = my_string.lower()  # 대문자를 소문자로 바꾸기
    arr_alphabet_lower = sorted(alphabet_lower) # 소문자로 바꾼 문자를 정렬하기
    answer = "".join(arr_alphabet_lower)    # 리스트화 됐으니, join으로 한 번에 모아서 쓰기
    
    return answer
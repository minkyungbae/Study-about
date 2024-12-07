def solution(array):
    set_array = list(set(array))    # set 함수 써서 중복값 없앤 후 리스트 변환
    max_count = 0                   # 처음 비교값 기준
    answer = -1                     # 빈도값이 같을 때 쓸 거임(굳이 안 만들어도 됐음)
    
    for num in set_array:
        count_array = array.count(num)  #count 함수를 사용해서 배열의 빈도를 구했음
        if max_count < count_array:     #최빈값 비교
            max_count = count_array     
            answer = num            #최빈값 구하기
        elif max_count == count_array:  #최빈값이 같은 애들일 때
            answer = -1
            
    return answer

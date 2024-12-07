def solution(n):
    numbers = []                                    # 리스트 만들기
    for num in range(n+1):
        if num % 2 != 0:                            # 홀수값 찾기
            numbers.append(num)                     # 리스트에 홀수값 넣기
    
    return numbers
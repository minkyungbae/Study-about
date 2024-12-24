def solution(n):
    numbers = []                                    # 리스트 만들기
    for num in range(1,n+1, 2):                     # 홀수값 찾기
        numbers.append(num)                         # 리스트에 홀수값 넣어주기
        
    return numbers
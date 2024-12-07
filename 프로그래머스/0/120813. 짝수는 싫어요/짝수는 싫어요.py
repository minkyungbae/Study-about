def solution(n):
    numbers = []                                    # 리스트 만들기
    for num in range(n+1):
        if num % 2 != 0:                            # 홀수값 찾기
            numbers.append(num)                     # 리스트에 홀수값 넣기
    
    return numbers


# range() 함수 쓰면 if 굳이 안 해도 됨
def solution(n):
    numbers = []                                    # 리스트 만들기
    for num in range(1,n+1, 2):                     # range() 함수를 써서 홀수값 찾기
        numbers.append(num)                         # append() 함수를 써서 리스트에 홀수값 넣어주기
    return numbers

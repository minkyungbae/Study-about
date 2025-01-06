# 인덱스 번호 알아내기 문제
def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
        
    return answer
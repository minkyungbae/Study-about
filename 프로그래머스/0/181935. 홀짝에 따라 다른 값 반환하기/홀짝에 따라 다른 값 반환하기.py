def solution(n):
    if n%2:                         # 홀수
        return sum(range(1,n+1,2))  # n 아래의 홀수들의 합
    return sum([i*i for i in range(2, n+1, 2)])  # 짝수면 제곱의 합
def solution(n):
    answer = []
    fac = 1 # 곱해줘야 하니까 1부터 시작
    
    for i in range(1,11):   # 최대 팩토리얼은 10
        fac *= i    # 팩토리얼 코드
        if fac <= n:    # 10! 값보다 작아야 함
            answer.append(i)
        
    return answer[-1]
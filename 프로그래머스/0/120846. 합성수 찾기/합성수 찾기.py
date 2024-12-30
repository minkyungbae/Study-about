def solution(n):
    answer = 0
    
    for j in range(2, n+1): # 2부터 시작하는 n+1까지의 범위
        num = 0 # 초기화
        for i in range(1, n+1): # 1부터 시작하는 n+1까지의 범위
            if j % i ==0:   # 약수 구하는 코드
                num +=1
            if num >=3: # num의 숫자가 3개 이상이 된다면 합성수를 의미
                answer +=1  # 그 경우만 answer에 +1을 해줌
                break
                
    return answer

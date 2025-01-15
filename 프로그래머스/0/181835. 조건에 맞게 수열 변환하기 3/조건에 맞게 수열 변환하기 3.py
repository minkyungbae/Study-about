def solution(arr, k):
    answer = []
    
    for i in arr:
        if k % 2 != 0:              #k가 홀수일 때 각각의 arr에 k 곱하기
            answer.append(i*k)
        else:                       #k가 짝수일 때 각각의 arr에 k 더하기
            answer.append(i+k)
            
    return answer
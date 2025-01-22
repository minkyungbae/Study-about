def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())    # 짝수번째면 소문자화
        else:
            answer.append(strArr[i].upper())    # 홀수번째면 대문자화
            
    return answer
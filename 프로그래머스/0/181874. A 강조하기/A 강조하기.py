def solution(myString):
    answer = ''
    
    for i in myString:
        if i == 'a':
            answer += i.upper()
        elif i == 'A':
            answer += 'A'
        else:
            answer += i.lower()
            
    return answer
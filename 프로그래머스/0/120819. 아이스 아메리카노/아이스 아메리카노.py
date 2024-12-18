def solution(money):
    answer = []
    coffee = money % 5500
    
    if coffee == 0:
        answer = [money // 5500, 0]
    
    else:
        answer = [money // 5500, money % 5500]

    return answer
import math

def solution(price):
    if price >= 500000:
        answer = price - price * 0.2
        
    elif price >= 300000:
        answer = price - price * 0.1
        
    elif price >= 100000:
        answer = price - price * 0.05 
    
    else:
        answer = price
        
    return int(math.trunc(answer))  #.trunc()는 소수점 버림
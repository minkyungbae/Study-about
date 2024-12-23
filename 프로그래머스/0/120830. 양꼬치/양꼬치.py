def solution(n, k):
    price = n*12000 + k*2000
    
    if k > 0 and n >= 10:
        price = n*12000 + (k-n//10)*2000
    return price
def solution(bin1, bin2):
    answer = ''
    
    answer = int(bin1, 2) + int(bin2, 2)
    
    return bin(answer)[2:]  # bin() <- 이걸 쓰면 앞에 "0b"가 생겨서 슬라이싱 했음

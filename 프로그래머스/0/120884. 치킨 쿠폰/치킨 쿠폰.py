def solution(chicken):
    service = 0
    
    while chicken >= 10:                   # 쿠폰이 10장 이상일 때부터 조건 시작
        service += chicken // 10           # 서비스 시킬 때는 쿠폰 10장 필요
        chicken = chicken % 10 + chicken // 10   #10장 단위로 써서 %, 서비스에서도 쿠폰 발생
        
    return service
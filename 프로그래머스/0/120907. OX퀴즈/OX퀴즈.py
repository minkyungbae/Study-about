# quiz는 문자열 배열
# 1. 계산을 위해선 int화 필요
# 2. 연산 기호와 숫자 사이 하나의 공백 존재 (split로 값 구분 필요)
# 3. 계산 결과를 O, X 출력

def solution(quiz):
    # 정답을 담을 리스트
    answer = []
    
    # quiz를 순회
    for q in quiz:
        # quiz는 "X [연산자] Y = Z"의 형태
        # op = operator(연산자)
        x, op, y, _, z = q.split()
        
        # int화
        x = int(x)
        y = int(y)
        z = int(z)
        
        # 연산자가 + 일 때의 처리 코드
        if op == "+":
            answer.append("O" if x + y == z else "X")
            
        # 연산자가 - 일 때의 처리 코드
        else:
            answer.append("O" if x - y == z else "X")
            
    return answer
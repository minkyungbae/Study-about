def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers[-1])  # 원하는 위치 i 앞에 추가할 값을 삽입
        numbers.pop()  # pop 함수는 ()에 아무 값도 넣지 않으면 마지막 인덱스를 삭제
        return numbers
        
    else:
        numbers.append(numbers[0])  # 맨 마지막 위치로 첫 번째 숫자가 추가됨
        numbers.pop(0)  # 첫 번째 값이 삭제
        return numbers
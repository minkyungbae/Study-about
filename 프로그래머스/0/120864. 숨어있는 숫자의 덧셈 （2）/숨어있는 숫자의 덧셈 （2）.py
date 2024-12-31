def solution(my_string):

    answer = ''.join(i if i.isdigit() else ' ' for i in my_string)
    # my_string에서 isdigit() 함수를 통해, 숫자를 ''에 기입
    # 숫자가 아닐 경우 공백으로 ''에 기입
    return sum(int(i) for i in answer.split())
    # 공백으로 나눈 answer를 split()으로 구분하여 숫자를 sum
    # i는 ''문자열화이기 때문에 int로 변환
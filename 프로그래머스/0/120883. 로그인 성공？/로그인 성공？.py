def solution(id_pw, db):
    for i in db:
        if id_pw[0] in i:           # 아이디가 db에 있는 경우
            if id_pw[1] == i[1]:    # 비밀먼호까지 맞을 경우
                return "login"
            else:                   # 비밀번호가 다를 경우
                return "wrong pw"
                       
    return "fail"                   # 아이디, 비밀번호가 db에 없는 경우
            
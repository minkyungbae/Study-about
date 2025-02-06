def solution(myString, pat):
    myString = ''.join([
        "B" if i == "A" else "A" for i in myString
    ])
    
    return 1 if pat in myString else 0
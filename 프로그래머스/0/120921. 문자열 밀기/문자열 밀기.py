def solution(A, B):

    for i in range(len(A)):         # len(A) 만큼 돌아가면서 재배열
        if A == B:                  # 만약 재배열되더라도 A와 B가 같으면
            return i                # 횟수를 찾기 위한 코드
        A = A[-1] + A[:-1]          # 맨 마지막에 있던 문자가 맨 앞으로 오고, 처음부터 끝까지를 이어붙이면 A 완성
    
    return -1
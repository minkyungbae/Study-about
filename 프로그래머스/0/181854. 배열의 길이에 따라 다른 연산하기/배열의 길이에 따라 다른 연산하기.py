def solution(arr, n):
    # 배열의 길이가 홀수인지 짝수인지 확인
    if len(arr) % 2 == 1:
        # 배열의 길이가 홀수라면 짝수 인덱스에 n을 더함
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        # 배열의 길이가 짝수라면 홀수 인덱스에 n을 더함
        for i in range(1, len(arr), 2):
            arr[i] += n
            
    return arr
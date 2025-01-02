def solution(array, n):
    array.sort()
    sub_array = []
    
    for i in range(len(array)):
        sub_array.append(abs(n - array[i])) # abs(n - array[i])의 결괏값을 그대로 객체에 추가
        
    return array[sub_array.index(min(sub_array))]

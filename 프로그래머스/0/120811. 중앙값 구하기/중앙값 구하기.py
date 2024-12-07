def solution(array):
    sort_array = sorted(array)
    center_num = len(array) // 2
    answer = sort_array[center_num]
    return answer
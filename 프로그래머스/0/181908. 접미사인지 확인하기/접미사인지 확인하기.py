def solution(my_string, is_suffix):
    slic = [my_string[i:] for i in range(len(my_string))]
        
    for i in slic:
        if is_suffix == i:
            return 1
    return 0
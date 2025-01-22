def solution(my_string, is_prefix):
    slic = [my_string[:i] for i in range(len(my_string))]
    
    for i in slic:
        if is_prefix == i:
            return 1
    return 0
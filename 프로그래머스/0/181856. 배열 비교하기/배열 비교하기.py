def solution(arr1, arr2):
    # 길이 비교
    if len(arr1) > len(arr2):   
        return 1
    
    elif len(arr1) < len(arr2):
        return -1
    
    # 길이가 같을 때
    else:
        if sum(arr1) > sum(arr2):
            return 1
        
        elif sum(arr1) < sum(arr2):
            return -1
        # 길이도, 합도 같을 때
        else:
            return 0
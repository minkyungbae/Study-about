def solution(my_string):
    answer = ''
    collection = ("a", "e","i","o","u")
    
    for i in collection:
        my_string = my_string.replace(i,'')
            
    return my_string
def solution(my_string, letter):
    answer = ''
    
    for i in my_string:
        answer = my_string.replace(letter, '') 
        
    return answer

# .replace() : 교환
# .replace(바꾸려는 문자, 어떻게 바꿀 것인지)
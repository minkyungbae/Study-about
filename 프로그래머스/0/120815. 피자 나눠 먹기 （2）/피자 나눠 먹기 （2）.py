def solution(n):
    pizza_piece = 6
    
    while True:
        if pizza_piece % n != 0:
            pizza_piece = pizza_piece +6

        elif pizza_piece % n == 0:
            answer = pizza_piece/6
            break
    return int(answer)
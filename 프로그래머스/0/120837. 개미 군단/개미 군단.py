def solution(hp):
    general_ant_count = hp//5
    soldier_ant_count = (hp - (5*general_ant_count))//3
    worker_ant_count = (hp - (5*general_ant_count) -(3*soldier_ant_count))//1
    answer = general_ant_count + soldier_ant_count + worker_ant_count
    return answer
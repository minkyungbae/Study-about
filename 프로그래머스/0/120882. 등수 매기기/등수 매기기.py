def solution(score):
    answer = []
    avg = []
    
    for i in score:                         # 각 점수들의 평균들 구하기
        avg.append(sum(i)/len(i))
        arr_avg = sorted(avg, reverse=True) # 내림차순으로 정렬하기
        
    for i in avg:                           # 등수 매기기
        answer.append(arr_avg.index(i)+1)   # index는 0부터 시작해서 +1을 해줌
    return answer
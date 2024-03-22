# 명예의 전당 

def solution(k, score):
    answer = []  # 각 단계에서 k개의 최고 점수 중 가장 낮은 점수를 저장할 리스트
    
    output_score = []  # 현재까지의 최고 점수 k개를 저장할 리스트
    
    for i in score:  # 주어진 점수 리스트를 순회
        if len(output_score) < k:  # output_score에 저장된 점수의 수가 k보다 작으면
            output_score.append(i)  # 점수를 output_score에 추가
        else:  # output_score에 k개의 점수가 이미 저장되어 있으면
            if min(output_score) < i:  # 현재 점수가 output_score의 최소값보다 크면
                output_score.remove(min(output_score))  # output_score에서 최소값 제거
                output_score.append(i)  # 현재 점수를 output_score에 추가
        
        answer.append(min(output_score))  # output_score의 최소값을 answer에 추가
                
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
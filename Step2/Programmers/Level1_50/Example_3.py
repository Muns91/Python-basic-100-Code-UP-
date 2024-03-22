def solution(name, yearning, photo):
    answer = []
    
    # 루가 사진을 본다
    for picture in photo:
        
        score = 0
        
        for i in picture:
            
            for j in range(len(name)):
                
                if i == name[j]:
                    score += int(yearning[j])
                    
        answer.append(score)
                        
            
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))


# def solution(name, yearning, photo):
#     # 이름과 갈망 점수를 매핑하는 딕셔너리 생성
#     name_to_yearning = {n: y for n, y in zip(name, yearning)}
#     answer = []

#     for picture in photo:
#         score = sum(name_to_yearning.get(person, 0) for person in picture)
#         answer.append(score)

#     return answer

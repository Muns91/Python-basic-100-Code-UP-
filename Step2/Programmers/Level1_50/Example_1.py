# 콜라 문제

def solution(a, b, n):
    answer = 0  # 마실 수 있는 콜라의 총량
    
    # 처음에 가진 병의 수가 a개 미만이 될 때까지 반복
    while n >= a:
        # a개로 교환할 때 남는 병의 수 계산
        bottle = n % a  # 남은 병 수
        
        # a개의 병으로 교환한 후 남은 새 병의 수 계산
        n = (n // a) * b
        answer += n  # 마신 콜라의 총량에 추가
        
        # 교환 후 남은 병과 교환으로 얻은 새 병을 합침
        n += bottle
    
    return answer


print(solution(2, 1, 20))
print(solution(3, 1, 20))
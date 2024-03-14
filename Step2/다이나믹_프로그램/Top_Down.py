# 메모이제이션을 위한 딕셔너리 초기화
memo = {}

# 탑다운 다이나믹 프로그래밍을 이용한 피보나치 수 계산
def fibonacci_top_down(n):
    # 이미 계산된 값이면 메모에서 반환
    if n in memo:
        return memo[n]
    # 피보나치 기본 케이스
    if n <= 2:
        return 1
    # 재귀적으로 결과 계산 및 메모에 저장
    memo[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return memo[n]

# 예제 사용
print(fibonacci_top_down(10))  # 55 출력

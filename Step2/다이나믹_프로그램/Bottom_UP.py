# 보텀업 다이나믹 프로그래밍을 이용한 피보나치 수 계산
def fibonacci_bottom_up(n):
    # 첫 두 피보나치 수는 1
    if n <= 2:
        return 1
    fib_table = [0] * (n + 1)  # 결과 저장을 위한 테이블 초기화
    fib_table[1], fib_table[2] = 1, 1  # 초기값 설정
    for i in range(3, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

# 예제 사용
print(fibonacci_bottom_up(10))  # 55 출력

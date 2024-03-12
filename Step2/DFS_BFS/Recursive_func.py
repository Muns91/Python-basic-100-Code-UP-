def factorial(n):
    # 기저 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # n이 0보다 크면 n * (n-1)!을 반환
    else:
        return n * factorial(n - 1)

# 예제 사용
print(factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120 출력

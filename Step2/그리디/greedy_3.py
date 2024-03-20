# n, m을 공백으로 구분하여 입력받음. n은 행의 개수, m은 열의 개수를 의미한다.
n, m = map(int, input().split())

# 최종 결과를 저장할 변수를 0으로 초기화한다. 이 변수는 각 행에서 선택된 가장 작은 수들 중 가장 큰 수를 저장한다.
result = 0

# n번 반복하여 각 행을 입력받고 처리한다.
for i in range(n):
    # 현재 행의 숫자들을 공백으로 구분하여 입력받아 리스트로 만든다.
    data = list(map(int, input().split()))

    # 현재 행에서 가장 작은 수를 찾는다.
    min_value = min(data)

    # 지금까지 찾은 가장 작은 수들 중에서 가장 큰 수와 현재 행의 가장 작은 수를 비교하여 더 큰 값을 result에 저장한다.
    result = max(result, min_value)

# 최종적으로 result에 저장된 값을 출력한다. 이 값은 각 행에서 가장 작은 수들 중 최대값이다.
print(result)

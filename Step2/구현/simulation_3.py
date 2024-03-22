# 사용자로부터 시작 위치를 입력받음 (예: a1)
start_point = input()
# 입력받은 위치의 행 번호를 계산 ('1'에서 '8' 사이의 숫자)
row = int(start_point[1])
# 입력받은 위치의 열 번호를 계산 ('a'에서 'h' 사이의 알파벳을 1에서 8 사이의 숫자로 변환)
colunm = int(ord(start_point[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, -1)]

# 이동 가능한 위치의 수를 저장할 변수 초기화
result = 0

# 가능한 모든 이동 방향에 대해 반복
for step in steps:
    # 다음 위치의 행 계산
    next_row = row + step[0]
    # 다음 위치의 열 계산
    next_column = colunm + step[1]

    # 다음 위치가 체스판 안에 있는지 확인 (1에서 8 사이의 행과 열)
    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <=8:
        # 체스판 안에 있다면, 이동 가능한 위치의 수 증가
        result += 1

# 최종적으로 계산된 이동 가능한 위치의 수 출력
print(result)

# 공간의 크기 입력받기
space_size = int(input())
move_plan = input().split()
position_x, position_y = 1, 1

# 각 방향에 따른 x, y의 변화량
delta_x = [0, 0, -1, 1]
delta_y = [-1, 1, 0, 0]
directions = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in move_plan:
    # 이동 후 좌표 계산
    for i in range(len(directions)):
        if plan == directions[i]:
            next_x = position_x + delta_x[i]
            next_y = position_y + delta_y[i]
    # 공간을 벗어나는 경우 무시
    if next_x < 1 or next_y < 1 or next_x > space_size or next_y > space_size:
        continue
    # 이동 수행
    position_x, position_y = next_x, next_y

print(position_x, position_y)

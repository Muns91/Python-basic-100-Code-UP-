# 입력 받기: 맵의 크기 (n, m), 캐릭터의 초기 위치와 바라보는 방향 (x, y, direction)
n, m = map(int, input().split())
# 방문한 위치를 저장할 맵 초기화
d = [[0]* m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1  # 시작 위치 방문 처리

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시작 시 방문한 칸의 수는 1
count = 1
# 회전한 횟수
turn_time = 0

# 메인 로직 시작
while True:
    turn_left()  # 일단 왼쪽으로 회전
    nx = x + dx[direction]  # 이동할 x 좌표
    ny = y + dy[direction]  # 이동할 y 좌표

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1  # 해당 칸 방문 처리
        x = nx
        y = ny
        count += 1  # 방문한 칸의 수 증가
        turn_time = 0  # 회전 횟수 초기화
        continue

    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]  # 뒤로 이동
        ny = y - dy[direction]

        # 뒤가 이동 가능한 공간인 경우 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break  # 뒤가 막혀 있으면 탐색 종료
        turn_time = 0

# 방문한 칸의 수 출력
print(count)

n = int(input()) # 격자의 크기를 입력받음
grid = [list(map(int, input().split())) for _ in range(n)] # 격자 상태 입력받음
cy, cx = n//2, n//2 # 토네이도 시작 위치 (중앙)
dir = 0 # 현재 방향 (0: 왼쪽, 1: 아래, 2: 오른쪽, 3: 위)

# 이동 방향 정의 (왼쪽, 아래, 오른쪽, 위)
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# 토네이도로 인해 모래가 흩날릴 방향 저장 (각 방향에 대한 상대 위치)
tornado_dirs = [
    [[-2, 0], [2, 0], [-1, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [0, -2], [0, -1]],
    [[0, -2], [0, 2], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1], [2, 0], [1, 0]], 
    [[2, 0], [-2, 0], [1, -1], [-1, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [0, 2], [0, 1]],
    [[0, 2], [0, -2], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, -1], [-2, 0], [-1, 0]]
]
tornado = [0.02, 0.01, 0.07, 0.1] # 모래가 흩날리는 비율

move = [1, 0] # 이동 횟수와 방향 전환 카운터

frag = False # 루프 종료 조건
ans = 0 # 격자 밖으로 나간 모래의 양

while True:
    if frag: # 종료 조건 확인
        break
    for _ in range(move[0]): # 현재 방향으로 이동
        cy += dirs[dir][0]
        cx += dirs[dir][1]

        if [cy, cx] == [0, 0]: # 최종 위치 도달 시 루프 종료
            frag = True
        
        sand = grid[cy][cx] # 현재 위치의 모래 양
        grid[cy][cx] = 0 # 현재 위치 모래 제거

        alpha = 0 # 격자 밖으로 나간 모래 계산을 위한 변수

        # 모래 분산 시키기
        for t in range(len(tornado)):
            for t2 in range(2):
                alpha += int(sand * tornado[t])
                ty, tx = cy + tornado_dirs[dir][2*t+t2][0], cx + tornado_dirs[dir][2*t+t2][1]
                if 0 <= ty < n and 0 <= tx < n:
                    grid[ty][tx] += int(sand * tornado[t]) 
                else:
                    ans += int(sand * tornado[t])
        # 격자 밖으로 나간 모래와 남은 모래(알파) 처리
        ty, tx =  cy + tornado_dirs[dir][8][0], cx + tornado_dirs[dir][8][1]
        alpha += int(sand * 0.05)
        if 0 <= ty < n and 0 <= tx < n:
            grid[ty][tx] += int(sand * 0.05)
        else:
            ans += int(sand * 0.05)

        ly, lx = cy + tornado_dirs[dir][9][0], cx + tornado_dirs[dir][9][1]
        if 0 <= ly < n and 0 <= lx < n:
            grid[ly][lx] += sand - alpha
        else:
            ans += sand - alpha
        
    # 방향과 이동 횟수 업데이트
    dir += 1
    if dir == 4: dir = 0
    move[1] += 1
    if move[1] == 2:
        move[0] += 1
        move[1] = 0

print(ans) # 격자 밖으로 나간 모래의 총량 출력

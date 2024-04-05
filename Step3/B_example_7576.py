from collections import deque

# 상자의 크기 입력
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우 방향 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 모든 익은 토마토의 위치를 찾아 큐에 넣기
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

# BFS 실행
def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

bfs()

# 모든 토마토가 익는데 걸리는 시간 계산
max_days = 0
for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit()
        max_days = max(max_days, tomato)

print(max_days - 1) # 첫 날을 제외해야 하므로 -1

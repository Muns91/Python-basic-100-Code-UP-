from collections import deque

# 행(n)과 열(m)의 입력을 받습니다
n, m = map(int, input().split())

array = []

# 미로 입력 받기, 0은 벽이고 1은 길입니다
for i in range(n):
    array.append(list(map(int, input())))

print(array)

# 이동 방향 정의: 상, 하, 우, 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선 탐색(bfs) 함수로 최단 경로 찾기
def bfs(x, y):
    # 시작점을 큐에 넣기
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 첫 번째 요소를 꺼냄
        x, y = queue.popleft()

        # 가능한 모든 이동(상, 하, 우, 좌)을 시도
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 경계를 넘어가는지 확인
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 해당 칸이 벽인 경우 건너뜀
            if array[nx][ny] == 0:
                continue
            
            # 유효한 이동인 경우, 해당 칸을 거리로 표시하고 큐에 추가
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))
    
    # 우측 하단 구석까지의 거리 반환
    return array[n-1][m-1]

# 시작점에서 우측 하단 구석까지의 최단 거리 출력
print(bfs(0,0))

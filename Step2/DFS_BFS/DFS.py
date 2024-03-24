# 맵의 크기 입력 받기
n, m = map(int, input().split())

# 그래프 초기화
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))  # 그래프 정보 입력 받기

# DFS 함수 정의
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x<=-1 or x >=n or y<=-1 or y>=m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1  # 해당 노드 방문 처리

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        # 연결된 모든 노드를 방문했다면 True 반환
        return True
    # 이미 방문했거나 벽인 경우 False 반환
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1  # 새로운 연결 요소 발견 시 카운트 증가

# 결과 출력
print(result)

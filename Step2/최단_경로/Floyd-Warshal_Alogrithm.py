def floyd_warshall(weights):
    n = len(weights)
    # 최단 거리 정보를 저장할 2차원 리스트를 초기화합니다.
    dist = [[float('infinity') for _ in range(n)] for _ in range(n)]
    
    # 각 노드에서 자기 자신으로의 거리는 0입니다.
    for i in range(n):
        dist[i][i] = 0
    
    # 주어진 가중치를 바탕으로 초기 거리를 설정합니다.
    for i in range(n):
        for j in range(n):
            dist[i][j] = weights[i][j]

    # 각 노드를 거쳐 가는 경우를 고려하여 최단 거리를 갱신합니다.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # 모든 노드 쌍 간의 최단 거리를 반환합니다.
    return dist

# 그래프는 2차원 리스트로 표현됩니다. 무한대는 연결되지 않음을 의미합니다.
graph = [
    [0, 1, 4, float('infinity')],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [float('infinity'), 5, 1, 0]
]

print(floyd_warshall(graph))  # 모든 노드 쌍 간의 최단 거리를 출력

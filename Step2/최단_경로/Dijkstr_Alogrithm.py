def dijkstra(graph, start):
    # 모든 노드까지의 거리를 무한대로 초기화합니다.
    distances = {vertex: float('infinity') for vertex in graph}
    # 시작 노드까지의 거리는 0입니다.
    distances[start] = 0
    # 방문한 노드를 추적하기 위한 집합입니다.
    visited = set()

    # 아직 방문하지 않은 모든 노드를 방문할 때까지 반복합니다.
    while visited != set(graph.keys()):
        # 방문하지 않은 노드 중에서 가장 가까운 노드를 선택합니다.
        current_vertex = min((vertex for vertex in distances if vertex not in visited), key=lambda vertex: distances[vertex])
        
        # 선택된 노드의 이웃을 순회하며 거리를 업데이트합니다.
        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
        # 현재 노드를 방문한 것으로 표시합니다.
        visited.add(current_vertex)
    
    # 모든 노드까지의 최단 거리를 반환합니다.
    return distances

# 그래프는 딕셔너리로 표현되며, 간선의 가중치와 함께 저장됩니다.
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))  # 시작점 A에서 다른 모든 점까지의 최단 거리를 출력

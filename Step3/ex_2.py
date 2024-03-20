def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]  # 첫 번째 요소를 저장합니다. 이 값은 마지막에 사용됩니다.
    min_value = first  # 최소값을 초기에 첫 번째 요소로 설정합니다.
    
    # 왼쪽 열을 위로 이동시킵니다.
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_value = min(min_value, matrix[k+1][y1])  # 이동하는 동안 최소값을 업데이트합니다.
    
    # 아래쪽 행을 왼쪽으로 이동시킵니다.
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_value = min(min_value, matrix[x2][k+1])  # 이동하는 동안 최소값을 업데이트합니다.
        
    # 오른쪽 열을 아래로 이동시킵니다.
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_value = min(min_value, matrix[k-1][y2])  # 이동하는 동안 최소값을 업데이트합니다.
    
    # 위쪽 행을 오른쪽으로 이동시킵니다.
    for k in range(y2, y1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_value = min(min_value, matrix[x1][k-1])  # 이동하는 동안 최소값을 업데이트합니다.
        
    # 첫 번째 요소를 이동 경로의 끝으로 옮깁니다.
    matrix[x1][y1+1] = first
    
    return min_value  # 이동하는 동안 발견된 최소값을 반환합니다.

# rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]  

def solution(rows, columns, queries):
    # 초기 행렬을 생성합니다.
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    result = []  # 결과를 저장할 리스트입니다.

    # 각 쿼리를 순회하며 rotate 함수를 호출합니다.
    for x1, y1, x2, y2 in queries:
        # 회전 결과의 최소값을 결과 리스트에 추가합니다.
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))

    return result  # 결과 리스트를 반환합니다.

# 함수 호출 및 결과 출력
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))

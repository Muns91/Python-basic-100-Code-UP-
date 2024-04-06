# 2024년 4월 4일
# 행렬의 곱셈
# 유형 : 연습 문제

# 2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 함수를 완성하세요.

arr1=[[1, 4], [3, 2], [4, 1]]
arr2=[[3, 3], [3, 3]]

def solution(arr1, arr2):
    
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    print(r1, c1)
    print(r2, c2)
    
    ret = [[0]* c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]
                
    
            
            
            
    
    
    return ret

print(solution(arr1, arr2))
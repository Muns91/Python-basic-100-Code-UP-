def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m                
    
    for a in arr:
        count[a] += 1             # 각 숫자의 개수 세기
    i = 0
    for a in range(m):            
        for c in range(count[a]):  # 개수만큼 숫자를 결과에 추가
            arr[i] = a
            i += 1
    return arr

# 예제 사용
array = [4, 2, 2, 8, 3, 3, 1]
print("정렬된 배열:", counting_sort(array))

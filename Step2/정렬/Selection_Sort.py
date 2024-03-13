def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 가장 작은 원소의 인덱스를 찾음
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 찾은 최소값을 현재 위치로 이동
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 예제 사용
array = [64, 25, 12, 22, 11]
selection_sort(array)
print("정렬된 배열:", array)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 피벗 설정
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 요소
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 요소
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소
    return quick_sort(left) + middle + quick_sort(right)

# 예제 사용
array = [3, 6, 8, 10, 1, 2, 1]
print("정렬된 배열:", quick_sort(array))

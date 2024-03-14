def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid  # 원하는 값 x를 찾으면 그 위치를 반환
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # x를 찾지 못하면 -1 반환

# 예제 사용
arr = [1, 2, 3, 4, 5]  # 이진 탐색을 위해서는 배열이 정렬되어 있어야 합니다.
x = 3
result = binary_search(arr, x)
if result != -1:
    print(f"원소 {x}는 배열의 {result}번째 인덱스에 있습니다.")
else:
    print(f"원소 {x}는 배열에 없습니다.")

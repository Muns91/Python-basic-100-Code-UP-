def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # 원하는 값 x를 찾으면 그 위치를 반환
    return -1  # x를 찾지 못하면 -1 반환

# 예제 사용
arr = [1, 4, 2, 5, 3]
x = 5
result = sequential_search(arr, x)
if result != -1:
    print(f"원소 {x}는 배열의 {result}번째 인덱스에 있습니다.")
else:
    print(f"원소 {x}는 배열에 없습니다.")
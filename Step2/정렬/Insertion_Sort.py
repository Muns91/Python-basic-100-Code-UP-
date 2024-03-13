def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # 이전 요소들을 비교하며 적절한 위치 찾기
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

# 예제 사용
array = [12, 11, 13, 5, 6]
insertion_sort(array)
print("정렬된 배열:", array)

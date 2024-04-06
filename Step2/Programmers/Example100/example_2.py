# 2024년 4월 4일
# 배열 정렬하기

# 정수 배열하나를 받습니다.
# 배열의 중복값을 제거하고 배열 데이터를 내림차순으로 정렬해서 반환하는 solution() 함수를 구현하시오.

arr = list(map(int, input().split()))

arr=list(set(arr))

arr.sort(reverse=True)

print(arr)
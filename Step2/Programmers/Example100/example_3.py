# 2024년 4월 4일
# 두 개 뽑아서 더하기

# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 
# 모든 수를 배열에 오름차순으로 담아 반환하는 solution함수를 완성하시오.

arr = list(map(int, input().split()))

arr.sort()

ans = []

for i in range((len(arr))):
    for j in range(i+1, len(arr)):
        
        values = arr[i] + arr[j]
        ans.append(values)

ans = sorted(set(ans))
print(ans)

def max_non_adjacent_sum(nums):
    if not nums:
        return 0

    incl = 0  # 현재 수를 포함한 최대 합
    excl = 0  # 현재 수를 포함하지 않은 최대 합

    for num in nums:
        # 현재 수를 포함한 경우와 포함하지 않은 경우 중 더 큰 값을 선택
        new_excl = max(incl, excl)

        # 현재 수를 포함한 경우는 이전의 "포함하지 않은 최대 합 + 현재 수"
        incl = excl + num

        # 현재 수를 포함하지 않은 경우는 이전의 "현재 수를 포함한 최대 합 또는 포함하지 않은 최대 합"
        excl = new_excl

    # 최종적으로 두 경우 중 더 큰 값을 반환
    return max(incl, excl)

# 예시 입력
numbers = [1, 2, 9, 4]

# 결과 출력
result = max_non_adjacent_sum(numbers)
print("최대 수의 합:", result)

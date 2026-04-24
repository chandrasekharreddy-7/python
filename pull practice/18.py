def two_sum_sorted(numbers: list, target: int) -> list:
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
print(two_sum_sorted([2, 7, 11, 15], 9))     # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))          # [1, 3]
print(two_sum_sorted([-1, 0], -1))           # [1, 2]
print(two_sum_sorted([1, 2, 3, 4, 5], 9))    # [4, 5]
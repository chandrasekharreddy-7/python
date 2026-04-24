def subarray_sum(nums: list, k: int) -> int:
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total = total + nums[j]
            if total == k:
                count = count + 1
    return count
print(subarray_sum([1, 1, 1], 2))              # 2
print(subarray_sum([1, 2, 3], 3))              # 2
print(subarray_sum([1, -1, 0], 0))             # 3
print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # 4
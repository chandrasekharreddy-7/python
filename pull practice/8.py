def max_subarray(nums: list) -> int:
    current_sum = nums[0]
    best_sum = nums[0]
    for i in range(1, len(nums)):
        # Add current number to previous sum
        current_sum = current_sum + nums[i]
        # If current number alone is better, start new subarray
        if nums[i] > current_sum:
            current_sum = nums[i]
        # Update best sum
        if current_sum > best_sum:
            best_sum = current_sum
    return best_sum
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1]))                               # 1
print(max_subarray([5, 4, -1, 7, 8]))                  # 23
print(max_subarray([-2, -1]))                          # -1
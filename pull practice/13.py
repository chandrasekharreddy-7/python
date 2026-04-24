def longest_consecutive(nums: list) -> int:
    if len(nums) == 0:
        return 0
    nums = sorted(nums)
    longest = 1
    current_count = 1
    for i in range(1, len(nums)):
        # Skip duplicate numbers
        if nums[i] == nums[i - 1]:
            continue
        # Check consecutive number
        if nums[i] == nums[i - 1] + 1:
            current_count += 1
        else:
            current_count = 1
        if current_count > longest:
            longest = current_count
    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))          # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longest_consecutive([1, 2, 0, 1]))                    # 3
print(longest_consecutive([]))                              # 0
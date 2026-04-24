def contains_duplicate(nums: list) -> bool:
    unique_nums = set(nums)
    if len(nums) != len(unique_nums):
        return True
    else:
        return False
print(contains_duplicate([1, 2, 3, 1]))              # True
print(contains_duplicate([1, 2, 3, 4]))              # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2]))  # True
print(contains_duplicate([]))                        # False
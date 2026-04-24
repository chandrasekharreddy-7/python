def top_k_frequent(nums: list, k: int) -> list:
    return sorted(set(nums), key=nums.count, reverse=True)[:k]
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
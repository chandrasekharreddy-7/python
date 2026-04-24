def three_sum(nums: list) -> list:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    if triplet not in result:
                        result.append(triplet)
    return result
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 1, 1]))
print(three_sum([0, 0, 0]))
print(three_sum([-2, -1, 0, 1, 2]))
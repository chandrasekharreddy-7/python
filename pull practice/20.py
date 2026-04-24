def product_except_self(nums: list) -> list:
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product = product * nums[j]
        result.append(product)
    return result
print(product_except_self([1, 2, 3, 4]))        # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))   # [0, 0, 9, 0, 0]
print(product_except_self([2, 3, 5]))           # [15, 10, 6]
def move_zeroes(nums: list) -> None:
    result = []
    zero = []
    for num in nums:
        if num != 0:
            result.append(num)
        else:
            zero.append(num)
    nums[:] = result + zero


nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)
            

nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)   # [1, 3, 12, 0, 0]

nums2 = [0]
move_zeroes(nums2)
print(nums2)   # [0]

nums3 = [1, 0, 2, 0, 3]
move_zeroes(nums3)
print(nums3)   # [1, 2, 3, 0, 0]

nums4 = [0, 0, 0, 1]
move_zeroes(nums4)
print(nums4)   # [1, 0, 0, 0]
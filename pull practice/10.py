def max_area(height: list) -> int:
    left = 0
    right = len(height) - 1
    best_area = 0
    while left < right:
        width = right - left
        smaller_height = min(height[left], height[right])
        area = width * smaller_height
        if area > best_area:
            best_area = area
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best_area
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))                         # 1
print(max_area([4, 3, 2, 1, 4]))                # 16
print(max_area([1, 2, 1]))                      # 2
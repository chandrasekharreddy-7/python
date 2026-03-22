def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    root1 = (-b + (discriminant)**1/2) / (2 * a)
    root2 = (-b - (discriminant)**1/2) / (2 * a)
    if root1 > 0: return root1
    if root2 > 0: return root2
    return None
print(f"Positive root = {quadratic_roots(1, -3, 2)}")
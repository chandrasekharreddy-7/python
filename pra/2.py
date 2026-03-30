''' Quadratic Equation Solver:
    Write a function quadratic_roots that takes coefficients $(a, b, c)$ for the 
    equation $ax^{2}+bx+c=0$ and returns the positive real root if one exists; otherwise, 
    return None. '''
def check_quadratic(a, b, c):
    d = b ** 2 - (4 * a * c)
    r1 = (-b + d**0.5)/2*a
    r2 = (-b - d**0.5)/2*a
    if d < 0 or (r1 <= 0 and r2 <= 0):
        return None
    if d >= 0:
        if r1 > 0 and r2 > 0:
            return f"root1 = {r1} :  root2 = {r2}"
        elif r1 > 0:
            return f"roo1 = {r1}"
        elif r2 > 0:
            return f"root2 = {r2}"
        else:
            print(f"there are no positive roots.")
            return None
    return None
print(check_quadratic(1, -5, 6))
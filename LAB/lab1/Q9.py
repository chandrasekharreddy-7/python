def matmul(A, B, r1, c1, r2, c2):
    if c1 != r2:
        return "Not possible"

    result = [0] * (r1 * c2)

    for i in range(r1):
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += A[i*c1 + k] * B[k*c2 + j]
            result[i*c2 + j] = s
    return result
A = [1,2,3,4,5,6,7,8,9]
B = [9,8,7,6,5,4,3,2,1]
print(matmul(A, B, 3, 3, 3, 3))
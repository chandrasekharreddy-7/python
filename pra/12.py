''' Matrix Multiplication:
    Create a function matMul that multiplies two matrices stored in row-major order. '''
def matMul(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    if n != len(B):
        return "matrix multiplication not possible"
    C = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[1, 2, 3],
    [4, 5, 6]]
B = [[7, 8],
    [9, 10],
    [11, 12]]
result = matMul(A, B)
for row in result:
    print(row)
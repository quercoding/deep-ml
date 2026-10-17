import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = [0 for _ in range(len(A[0]))]
    for k in range(n):
        new_x = [0 for _ in range(len(A[0]))]
        for i in range(len(A)):
            total = 0
            for j in range(len(A[0])):
                if i != j:
                    total += A[i][j] * x[j]
            new_x[i] = (b[i] - total) / A[i][i]
        x = new_x
    return [round(v,4) for v in x]
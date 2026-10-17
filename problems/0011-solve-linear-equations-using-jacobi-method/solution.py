import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = [0.0] * len(b)
    for _ in range(n):
        x_new = [0.0] * len(b)
        for i in range(len(b)):
            total = 0.0
            for j in range(len(b)):
                if j != i:
                    total += A[i][j] * x[j]
            x_new[i] = (b[i] - total) / A[i][i]
        x = x_new
    return [round(v, 4) for v in x]
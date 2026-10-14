import numpy as np

def transform_matrix(A, T, S):
    if np.linalg.det(T) == 0:
        return -1
    if np.linalg.det(S) == 0:
        return -1

    T_inv = np.linalg.inv(T)

    result_1 = []
    for row in range(len(T_inv)):
        total = []
        for col in range(len(A[0])):
            sum = 0
            for k in range(len(A)):
                sum += T_inv[row][k] * A[k][col]
            total.append(sum)
        result_1.append(total)

    result_2 = []
    for row in range(len(result_1)):
        total = []
        for col in range(len(S[0])):
            sum = 0
            for k in range(len(S)):
                sum += result_1[row][k] * S[k][col]
            total.append(sum)
        result_2.append(total)
    return result_2

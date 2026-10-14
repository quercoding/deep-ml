def matrixmul(a, b):
    n_cols_a = len(a[0])
    n_rows_b = len(b)
    if n_cols_a != n_rows_b:
        return -1

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            s = 0
            for k in range(n_cols_a):
                s += a[i][k] * b[k][j]
            row.append(s)
        result.append(row)
    return result

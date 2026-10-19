def determinant_4x4(matrix: list[list[int | float]]) -> float:
    def det(M):
        n = len(M)
        if n == 1:
            return M[0][0]
        if n == 2:
            return M[0][0] * M[1][1] - M[0][1] * M[1][0]
        total = 0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in M[1:]]
            total += ((-1) ** j) * M[0][j] * det(minor)
        return total
    d = det([[float(x) for x in row] for row in matrix])
    if abs(d - round(d)) < 1e-9:
        return int(round(d))
    return d
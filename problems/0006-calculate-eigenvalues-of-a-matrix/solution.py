import math

def calculate_eigenvalues(matrix):
    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    root = math.sqrt(trace**2 - 4*det)
    eigen_1 = (trace + root) / 2
    eigen_2 = (trace - root) / 2
    result = [eigen_1, eigen_2]
    result.sort(reverse=True)
    return result
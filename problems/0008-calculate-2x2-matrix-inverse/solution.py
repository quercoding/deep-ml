def inverse_2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None
    if det != 0:
        return [ [matrix[1][1]/det,-matrix[0][1]/det],[-matrix[1][0]/det,matrix[0][0]/det]]

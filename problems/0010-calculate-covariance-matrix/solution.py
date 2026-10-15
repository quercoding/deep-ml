def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    average = []
    for i in range(len(vectors)):
        total = 0
        for j in range(len(vectors[0])):
            total += vectors[i][j]
        average.append(total / len(vectors[0]))

    result = []
    for i in range(len(vectors)):
        row = []
        for j in range(len(vectors)):
            total = 0
            for k in range(len(vectors[0])):
                total += (vectors[i][k] - average[i]) * (vectors[j][k] - average[j])
            row.append(total / (len(vectors[0]) - 1))
        result.append(row)
    return result
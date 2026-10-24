import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    data = np.asarray(data, dtype=float)
    mean = data.mean(axis=0)
    std = data.std(axis=0)
    std = np.where(std == 0, 1.0, std)
    Z = (data - mean) / std

    cov = np.cov(Z, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)

    order = np.argsort(-eigvals)
    eigvecs = eigvecs[:, order][:, :k]

    for j in range(eigvecs.shape[1]):
        col = eigvecs[:, j]
        nonzero = np.where(np.abs(col) > 1e-10)[0]
        if len(nonzero) > 0 and col[nonzero[0]] < 0:
            eigvecs[:, j] = -col

    return np.round(eigvecs, 4)
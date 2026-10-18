import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    A = np.asarray(A, dtype=float)
    ATA = A.T @ A
    b00, b01, b11 = ATA[0, 0], ATA[0, 1], ATA[1, 1]
    theta = 0.5 * np.arctan2(2.0 * b01, b00 - b11) if abs(b01) > 1e-15 else 0.0
    c, s = np.cos(theta), np.sin(theta)
    V = np.array([[c, -s], [s, c]])
    B = A @ V
    S = np.sqrt((B ** 2).sum(axis=0))
    idx = np.argsort(-S)
    S, B, V = S[idx], B[:, idx], V[:, idx]
    U = np.zeros((2, 2))
    for i in range(2):
        if S[i] > 1e-15:
            U[:, i] = B[:, i] / S[i]
    if S[0] <= 1e-15:
        U = np.eye(2)
    elif S[1] <= 1e-15:
        U[:, 1] = np.array([-U[1, 0], U[0, 0]])
    return U, S, V.T
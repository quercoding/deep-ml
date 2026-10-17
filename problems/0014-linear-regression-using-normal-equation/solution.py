import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    Xt = X.T
    theta = np.linalg.inv(Xt @ X) @ Xt @ y
    return [round(v, 4) for v in theta]
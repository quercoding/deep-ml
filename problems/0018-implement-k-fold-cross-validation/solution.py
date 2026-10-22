import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)

    base = n_samples // k
    extra = n_samples % k
    sizes = [base + (1 if i < extra else 0) for i in range(k)]

    folds = []
    start = 0
    for s in sizes:
        folds.append(indices[start:start + s])
        start += s

    result = []
    for i in range(k):
        parts = [folds[j] for j in range(k) if j != i]
        train = np.concatenate(parts) if parts else np.array([], dtype=int)
        result.append((train.tolist(), folds[i].tolist()))
    return result
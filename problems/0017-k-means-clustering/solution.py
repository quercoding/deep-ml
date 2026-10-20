def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = [tuple(float(c) for c in cent) for cent in initial_centroids]
    pts = [tuple(float(x) for x in p) for p in points]

    for _ in range(max_iterations):
        labels = []
        for p in pts:
            best, best_d = 0, float("inf")
            for i, c in enumerate(centroids):
                d = sum((p[j] - c[j]) ** 2 for j in range(len(p)))
                if d < best_d:
                    best, best_d = i, d
            labels.append(best)

        new_c = []
        for i in range(len(centroids)):
            members = [p for p, l in zip(pts, labels) if l == i]
            if not members:
                new_c.append(centroids[i])
            else:
                dim = len(centroids[i])
                new_c.append(tuple(sum(m[d] for m in members) / len(members) for d in range(dim)))

        if new_c == centroids:
            break
        centroids = new_c

    return [tuple(round(v, 4) for v in c) for c in centroids]
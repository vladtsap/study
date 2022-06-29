import numpy as np


def calculate_distance(p1, p2):
    return np.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))


def assign_item_centroid(centroids, image: np.array):
    centroids_dict = {
        center: []
        for center in range(centroids.shape[0])
    }

    for i in range(image.shape[0]):
        distance = [calculate_distance(image[i], centroids[center]) for center in range(centroids.shape[0])]
        idx = distance.index(min(distance))
        centroids_dict[idx].append(image[i])
        image[i] = centroids[idx]

    return centroids_dict


def compute_centroids_means(centroids, centroid_dict):
    j = 0
    for cluster in centroid_dict:
        r, g, b = [0, 0, 0]
        cnt = 1
        for values in centroid_dict[cluster]:
            r += values[0]
            g += values[1]
            b += values[2]
            cnt += 1
        r /= cnt
        g /= cnt
        b /= cnt
        centroids[j] = [r, g, b]
        j += 1
    return centroids


def k_mean(image: np.ndarray, k=2, iterations=1) -> np.ndarray:
    w, h, c = image.shape

    # reshaping the image into 1d array with values r,g,b
    image = image.reshape(w * h, c)

    idx = [np.random.randint(w * h) for _ in range(k)]
    centroids = image[idx, :]

    for i in range(iterations):
        centroids = compute_centroids_means(
            centroids, assign_item_centroid(centroids, image),
        )

    return image.reshape(w, h, c)

import numpy as np
from numpy import ndarray


def mean_filtering(image: ndarray, ws=2) -> ndarray:
    for i in range(ws // 2, image.shape[0] - ws // 2):
        for j in range(ws // 2, image.shape[1] - ws // 2):
            for c in range(image.shape[2]):
                image[i][j][c] = np.mean(image[i - ws // 2: i + ws // 2 + 1, j - ws // 2: j + ws // 2 + 1, c])

    return image

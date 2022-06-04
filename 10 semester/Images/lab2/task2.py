import numpy as np
from numpy import ndarray


def mean_filtering(image: ndarray, ws=2) -> ndarray:
    for i in range(ws // 2, image.shape[0] - ws // 2):
        for j in range(ws // 2, image.shape[1] - ws // 2):
            for c in range(image.shape[2]):
                image[i][j][c] = np.mean(image[i - ws // 2: i + ws // 2 + 1, j - ws // 2: j + ws // 2 + 1, c])

    return image


def gaussian_filtering(image: ndarray, ws=9, sigma=2) -> ndarray:
    x = np.arange(-ws // 2 + 1, ws // 2 + 1)  # x = [0, 1, 2]    if window size is 3x3
    y = np.arange(-ws // 2 + 1, ws // 2 + 1)  # y = [0, 1, 2]    if window size is 3x3
    x, y = np.meshgrid(x, y, sparse=True)
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2)))  # G(x,y)
    gaussian_filter_value = g / g.sum()

    for i in range(ws // 2, image.shape[0] - ws // 2):
        for j in range(ws // 2, image.shape[1] - ws // 2):
            for c in range(image.shape[2]):
                image[i][j][c] = np.sum(
                    # CORRELATION
                    np.multiply(
                        (image[i - ws // 2: i + ws // 2 + 1, j - ws // 2: j + ws // 2 + 1, c]),
                        gaussian_filter_value,
                    )
                )

    return image

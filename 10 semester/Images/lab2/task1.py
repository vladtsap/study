import numpy as np
from numpy import ndarray


def gaussian_noise(image: ndarray, noise_sigma=22) -> ndarray:
    temp_image = np.float64(image)

    h = temp_image.shape[0]
    w = temp_image.shape[1]
    noise = np.random.randn(h, w) * noise_sigma

    noisy_image = np.zeros(temp_image.shape, np.float64)
    if len(temp_image.shape) == 2:
        noisy_image = temp_image + noise
    else:
        noisy_image[:, :, 0] = temp_image[:, :, 0] + noise
        noisy_image[:, :, 1] = temp_image[:, :, 1] + noise
        noisy_image[:, :, 2] = temp_image[:, :, 2] + noise

    return noisy_image


def bipolar_noise(image: ndarray, noise_prob=0.05) -> ndarray:
    rows, cols, _ = image.shape

    for i in range(rows):
        for j in range(cols):
            if np.random.random() < 0.5:
                if np.random.random() < noise_prob:
                    image[i][j] = [0, 0, 0]
            else:
                if np.random.random() < noise_prob:
                    image[i][j] = [255, 255, 255]

    return image

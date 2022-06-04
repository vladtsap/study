import numpy as np


def binarization(image: np.ndarray, threshold=180) -> np.ndarray:
    """converts the image to an image of 1 and 0"""
    img_width, img_height = image.shape

    for i in range(img_width):  # iterate through the img
        for j in range(img_height):
            image[i, j] = 255 if image[i, j] > threshold else 0

    return image

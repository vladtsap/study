import numpy as np


def binarization(image: np.ndarray, threshold=180) -> np.ndarray:
    """converts the image to an image of 1 and 0"""
    img_width, img_height = image.shape

    for i in range(img_width):  # iterate through the img
        for j in range(img_height):
            image[i, j] = 255 if image[i, j] > threshold else 0

    return image


def otsu(image: np.ndarray) -> np.ndarray:
    s, p1, p2, mu1, mu2, threshold = 0, 0, 0, 0, 0, 0

    hist, bins = np.histogram(image, 256)  # returns histogram as an array

    # while not at the end of the histogram calculate the sum
    # and mean from both sides of i from the graph then calculate the variance
    for i in range(1, 256):
        # calculate the sum
        p1 = np.sum(hist[:i])  # sum the values of the histogram to the left of col i
        p2 = np.sum(hist[i:])  # sum the values of the histogram to the right of col i

        # Calculate the mean
        mu1 = np.mean(hist[:i])  # get mean of values left of col i
        mu2 = np.mean(hist[i:])  # get mean of values right of col i

        # Calculate the variance
        variance = p1 * p2 * ((mu1 - mu2) ** 2)

        # if variance is greater than s then get new threshold
        if variance > s:
            s = variance
            threshold = i

    # after it calculates the threshold apply binarization with it
    return binarization(image, threshold)

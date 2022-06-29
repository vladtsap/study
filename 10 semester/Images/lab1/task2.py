from collections import defaultdict

from numpy import ndarray

from utils import normalize_pixel


def linear_contrasting(image: ndarray, contrasting_coefficient=400) -> ndarray:
    height, width, channels = image.shape

    # for finding low and high values at image
    brightness_min = 255
    brightness_max = 0

    for x in range(width):
        for y in range(height):
            pixel_brightness = sum(image[y, x]) / 3

            if pixel_brightness < brightness_min:
                brightness_min = pixel_brightness
            if pixel_brightness > brightness_max:
                brightness_max = pixel_brightness

    for x in range(width):
        for y in range(height):
            channel = image[y, x]

            pixel_brightness = sum(channel) / 3

            y_new = (pixel_brightness - brightness_min) / (brightness_max - brightness_min) * contrasting_coefficient
            diff = (pixel_brightness - y_new) / 3

            r, g, b = channel

            image[y, x] = [
                normalize_pixel(r - diff + 0.5), normalize_pixel(g - diff + 0.5), normalize_pixel(b - diff + 0.5)
            ]

    return image


def gamma_correction(image: ndarray, gamma=2.2) -> ndarray:
    def gamma_function(value: int) -> int:
        return normalize_pixel(255 * ((value / 255) ** (1 / gamma)))

    height, width, channels = image.shape

    for x in range(width):
        for y in range(height):
            r, g, b = image[y, x]

            image[y, x] = [gamma_function(r), gamma_function(g), gamma_function(b)]

    return image


def histogram_equalisation(image: ndarray, L=256) -> ndarray:
    def get_brightness(channel) -> int:
        return int(sum(channel) / 3)

    height, width, channels = image.shape

    counts = defaultdict(int)

    for x in range(width):
        for y in range(height):
            counts[get_brightness(image[y, x])] += 1

    for i in range(1, L):
        counts[i] += counts[i - 1]

    for x in range(width):
        for y in range(height):
            r, g, b = image[y, x]
            image[y, x] = [
                (L - 1) * (counts[r]) / (width * height),
                (L - 1) * (counts[g]) / (width * height),
                (L - 1) * (counts[b]) / (width * height),
            ]

    return image

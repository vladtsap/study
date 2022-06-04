from numpy import ndarray

from utils import normalize_pixel


def linear_contrasting(image: ndarray, contrasting_coefficient=400) -> ndarray:
    height, width, channels = image.shape

    # for finding low and high values at image
    brightness_min = 255
    brightness_max = 0

    for x in range(0, width):
        for y in range(0, height):
            pixel_brightness = sum(image[y, x]) / 3

            if pixel_brightness < brightness_min:
                brightness_min = pixel_brightness
            if pixel_brightness > brightness_max:
                brightness_max = pixel_brightness

    for x in range(0, width):
        for y in range(0, height):
            channel = image[y, x]

            pixel_brightness = sum(channel) / 3

            y_new = (pixel_brightness - brightness_min) / (brightness_max - brightness_min) * contrasting_coefficient
            diff = (pixel_brightness - y_new) / 3

            r, g, b = channel

            image[y, x] = [
                normalize_pixel(r - diff + 0.5), normalize_pixel(g - diff + 0.5), normalize_pixel(b - diff + 0.5)
            ]

    return image

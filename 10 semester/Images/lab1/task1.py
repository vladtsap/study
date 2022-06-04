from numpy import ndarray

LOWER_THRESH = 50
HIGHER_THRESH = 230


def balance_brightness(image: ndarray) -> ndarray:
    height, width, channels = image.shape

    for x in range(0, width):
        for y in range(0, height):
            channel = image[y, x]
            r, g, b = channel

            if all(channel <= [LOWER_THRESH] * 3):
                r += (LOWER_THRESH - r) / 2
                g += (LOWER_THRESH - g) / 2
                b += (LOWER_THRESH - b) / 2

            elif all(channel >= [HIGHER_THRESH] * 3):
                r += (HIGHER_THRESH - r) / 2
                g += (HIGHER_THRESH - g) / 2
                b += (HIGHER_THRESH - b) / 2

            image[y, x] = [r, g, b]

    return image

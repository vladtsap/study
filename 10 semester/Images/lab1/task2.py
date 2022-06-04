from numpy import ndarray

CONTRASTING_COF = 400


def linear_contrasting(image: ndarray) -> ndarray:
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

            y_new = (pixel_brightness - brightness_min) / (brightness_max - brightness_min) * CONTRASTING_COF
            diff = (pixel_brightness - y_new) / 3

            r, g, b = channel

            r_new = int(r - diff + 0.5)
            r_new = 255 if r_new > 255 else r_new
            r_new = 0 if r_new < 0 else r_new

            g_new = int(g - diff + 0.5)
            g_new = 255 if g_new > 255 else g_new
            g_new = 0 if g_new < 0 else g_new

            b_new = int(b - diff + 0.5)
            b_new = 255 if b_new > 255 else b_new
            b_new = 0 if b_new < 0 else b_new

            image[y, x] = [r_new, g_new, b_new]

    return image

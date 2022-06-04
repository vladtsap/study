from collections import deque

import numpy as np


def group_pixels(y_val, x_val, pix):
    # given a pixel, groups the neighbouring pixels together. returns group X,Y values.
    return np.mgrid[
           max(0, pix[0] - 1):min(y_val, pix[0] + 2),
           max(0, pix[1] - 1):min(x_val, pix[1] + 2),
           ].reshape(2, -1).T


def watershed(image: np.ndarray, levels=256) -> np.ndarray:
    image = np.array(image)
    mflag = False
    Nque = deque()  # label que
    curr_lbl = 0  # current label
    y_val, x_val = image.shape
    full_shape = y_val * x_val
    labels = np.full((y_val, x_val), -1, np.uint8)
    image_reshaped = image.reshape(full_shape)
    # for every pixel in the reshaped image, X,Y values of grouped pixels.
    pixels = np.mgrid[0:y_val, 0:x_val].reshape(2, -1).T
    neighbour_group = np.array([group_pixels(y_val, x_val, pix) for pix in pixels])
    neighbour_group = neighbour_group.reshape(y_val, x_val)
    index_values = np.argsort(image_reshaped)  # sorts the image, uses X,Y values
    image_sorted = image_reshaped[index_values]
    pixels_sorted = pixels[index_values]
    levels = np.linspace(image_sorted[0], image_sorted[-1], levels)  # space levels from 0 to 255.
    curr_lvl = 0
    level_index_values = []

    for i in range(full_shape):
        if image_sorted[i] > levels[curr_lvl]:
            while image_sorted[i] > levels[curr_lvl]: curr_lvl += 1
            level_index_values.append(i)
    first = 0
    level_index_values.append(full_shape)
    for last in level_index_values:
        for pixel in pixels_sorted[first:last]:
            labels[pixel[0], pixel[1]] = -2  # mask value
            for neighbour in neighbour_group[pixel[0], pixel[1]]:
                if labels[neighbour[0], neighbour[1]] >= 0:
                    labels[pixel[0], pixel[1]] = -3  # enqueue label
                    Nque.append(pixel)
                    break

        while Nque:
            pixel = Nque.popleft()
            for neighbour in neighbour_group[pixel[0], pixel[1]]:
                pixel_labels = labels[pixel[0], pixel[1]]
                neighbour_labels = labels[neighbour[0], neighbour[1]]
                if neighbour_labels > 0:
                    if pixel_labels == -3 or (pixel_labels == 0 and mflag):
                        labels[pixel[0], pixel[1]] = neighbour_labels
                    elif pixel_labels > 0 and pixel_labels != neighbour_labels:
                        labels[pixel[0], pixel[1]] = 0
                        mflag = False
                elif neighbour_labels == 0 and pixel_labels == -3:
                    labels[pixel[0], pixel[1]] = 0
                    mflag = True
                elif neighbour_labels == -2:
                    labels[neighbour[0], neighbour[1]] = -3
                    Nque.append(neighbour)

        for pixel in pixels_sorted[first:last]:
            if labels[pixel[0], pixel[1]] == -2:
                curr_lbl += 1
                Nque.append(pixel)
                labels[pixel[0], pixel[1]] = curr_lbl
                while Nque:
                    neighbour = Nque.popleft()
                    for curr_nbr in neighbour_group[neighbour[0], neighbour[1]]:
                        if labels[curr_nbr[0], curr_nbr[1]] == -2:
                            Nque.append(curr_nbr)
                            labels[curr_nbr[0], curr_nbr[1]] = curr_lbl
        first = last

    return labels

import numpy as np
from numpy import ndarray


def convolution(img, kernel):
    """
    Convolution
    Takes in the image and a kernel
    This method applies padding to the image then finds the correlation then convolve the kernel with the image
    returns the filtered image
    """
    img_w, img_h = img.shape  # get image dimensions
    kernel_w, kernel_h = kernel.shape  # get kernel dimensions
    filtered_image = np.ones((img_w, img_h))  # initialize output image

    # pad the image
    pad_x = (kernel_w - 1) // 2  # get the vertical pad length
    pad_y = (kernel_h - 1) // 2  # get the horizontal pad length
    pad_img = np.zeros((img_w + (2 * pad_x), img_h + (2 * pad_x)))  # fill the border with zeros
    pad_img_w, pad_img_h = pad_img.shape  # get dimensions of the new padded matrix
    pad_img[pad_x:pad_img_w - pad_x, pad_y:pad_img_h - pad_y] = img  # insert image into the padded matrix

    # iterate through the image; convolve the kernel and image patch by patch
    for i in range(img_w):
        for j in range(img_h):
            # get a patch of the image and multiply with the kernel
            # then sum up all the values to get a pixel value for the filtered image
            filtered_image[i, j] = np.sum(kernel * pad_img[i:i + kernel_w, j:j + kernel_h])

            # returns the filtered image
    return filtered_image


def sobel_filter(image: ndarray) -> (ndarray, ndarray, ndarray):
    # initialize sobel matrix to determine vertical edges
    matrix_y = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    kernel_y = np.asarray(matrix_y)
    # initialize sobel matrix to determine horizontal edges
    matrix_x = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    kernel_x = np.asarray(matrix_x)

    # apply the kernel to image by convolution
    filtered_image_y = convolution(image, kernel_y)
    filtered_image_x = convolution(image, kernel_x)

    filtered_image = np.sqrt(np.square(filtered_image_x) + np.square(filtered_image_y))

    # output the image
    return filtered_image_x, filtered_image_y, filtered_image

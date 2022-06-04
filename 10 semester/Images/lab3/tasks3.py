import cv2
import numpy as np

from lab3.task1 import convolution


def gaussianFilter(img, sigma):

    kernel = np.zeros((sigma, sigma))

    # iterate through the kernel window and apply the gaussian function
    for i in range(sigma):
        for j in range(sigma):
            kernel[i, j] = (1 / ((2 * np.pi * (sigma ** 2))) * np.exp(
                -(((i ** 2) + (j ** 2)) / (2 * (sigma ** 2)))))  # 2D Gaussian Function

    # Convolve the kernel with the image
    filtImg = convolution(img, kernel)

    # Scale the image
    scalefiltImg = 255 * (filtImg / np.max(filtImg))

    # Output the image
    # cv2.imwrite("Gaussian Filter s=" + str(sigma) + ".png", scalefiltImg)
    # saves image to files; same directory as this program


    # returns the blurred image; used in canny edge
    return scalefiltImg


def gradientOperations(img):

    # Backward Difference Convolution
    backDiffMatX = [[-1, 1], [-1, 1]]  # backward difference in x direction
    backDiffX = np.asarray(backDiffMatX)
    backDiffXImg = convolution(img, backDiffX)  # convole in x direction
    backDiffMatY = [[-1, -1], [1, 1]]  # backward difference in y direction
    backDiffY = np.asarray(backDiffMatY)
    backDiffYImg = convolution(img, backDiffY)  # convole in y direction

    # calculate magnitude
    backMagFiltImg = np.sqrt((backDiffXImg * backDiffXImg) + (backDiffYImg * backDiffYImg))

    # scale the X, Y and Mag images
    backDiffXImg = np.abs(backDiffXImg)
    backDiffYImg = np.abs(backDiffYImg)
    backDiffXImgScale = 255 * ((backDiffXImg - np.min(backDiffXImg)) / (np.max(backDiffXImg) - np.min(backDiffXImg)))
    backDiffYImgScale = 255 * ((backDiffYImg - np.min(backDiffYImg)) / (np.max(backDiffYImg) - np.min(backDiffYImg)))
    backDiffScaleImg = 255 * (
            (backMagFiltImg - np.min(backMagFiltImg)) / (np.max(backMagFiltImg) - np.min(backMagFiltImg)))

    # output X, Y and Mag images
    # cv2.imwrite("Gradient Operations Back X.png", backDiffXImgScale)
    # cv2.imwrite("Gradient Operations Back Y.png", backDiffYImgScale)
    # cv2.imwrite("Gradient Operations Back Magnitude Scaled.png", backDiffScaleImg)

    # --------------------------------------------------------------------------------------------------------------
    # Forward Difference Convolution
    forwardDiffMatX = [[1, -1], [1, -1]]  # forward difference in x direction
    forwardDiffX = np.asarray(forwardDiffMatX)
    forwardDiffXImg = convolution(img, forwardDiffX)  # convole in x direction
    forwardDiffMatY = [[1, 1], [-1, -1]]  # forward difference in y direction
    forwardDiffY = np.asarray(forwardDiffMatY)
    forwardDiffYImg = convolution(img, forwardDiffY)  # convole in y direction

    # calculate magnitude
    forwardMagFiltImg = np.sqrt(np.square(forwardDiffXImg) + np.square(forwardDiffYImg))

    # Scale X, Y, and Mag Images
    forwardDiffXImg = np.abs(forwardDiffXImg)
    forwardDiffYImg = np.abs(forwardDiffYImg)
    forwardXImgScale = 255 * (
            (forwardDiffXImg - np.min(forwardDiffXImg)) / (np.max(forwardDiffXImg) - np.min(forwardDiffXImg)))
    forwardYImgScale = 255 * (
            (forwardDiffYImg - np.min(forwardDiffYImg)) / (np.max(forwardDiffYImg) - np.min(forwardDiffYImg)))
    forwardDiffScaleImg = 255 * ((forwardMagFiltImg - np.min(forwardMagFiltImg)) / (
            np.max(forwardMagFiltImg) - np.min(forwardMagFiltImg)))

    # Output X, Y and Mag images
    # cv2.imwrite("Gradient Operations Forward X.png", forwardXImgScale)
    # cv2.imwrite("Gradient Operations Forward Y.png", forwardYImgScale)
    # cv2.imwrite("Gradient Operations Forward Magnitude Scaled.png", forwardDiffScaleImg)

    # --------------------------------------------------------------------------------------------------------------
    # Center Difference Convolution
    centerDiffMatX = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]  # center differece in x direction
    centerDiffX = np.asarray(centerDiffMatX)
    centerDiffXImg = convolution(img, centerDiffX)  # convole in x direction
    centerDiffMatY = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]  # center differece in y direction
    centerDiffY = np.asarray(centerDiffMatY)
    centerDiffYImg = convolution(img, centerDiffY)  # convole in y direction

    # Calculate Mag
    centerMagFiltImg = np.sqrt(np.square(centerDiffXImg) + np.square(centerDiffYImg))  # calculate magnitude

    # Scale X, Y, and Mag images
    centerDiffXImg = np.abs(centerDiffXImg)
    centerDiffYImg = np.abs(centerDiffYImg)
    centerXImgScale = 255 * (
            (centerDiffXImg - np.min(centerDiffXImg)) / (np.max(centerDiffXImg) - np.min(centerDiffXImg)))
    centerYImgScale = 255 * (
            (centerDiffYImg - np.min(centerDiffYImg)) / (np.max(centerDiffYImg) - np.min(centerDiffYImg)))
    centerDiffScaleImg = 255 * (
            (centerMagFiltImg - np.min(centerMagFiltImg)) / (np.max(centerMagFiltImg) - np.min(centerMagFiltImg)))

    # output X, Y, and Mag images
    # cv2.imwrite("Gradient Operations Center X.png", centerXImgScale)
    # cv2.imwrite("Gradient Operations Center Y.png", centerYImgScale)
    # cv2.imwrite("Gradient Operations Center Magnitude Scaled.png", centerDiffScaleImg)


    # returns the gradient orientation of the image; used in canny edge detector
    gradOrientation = np.degrees(np.arctan2(centerDiffYImg, centerDiffXImg))
    return (centerDiffScaleImg, gradOrientation)


def hysteresis(img):
    # initialize high and low thresholds
    highThreshold = 90
    lowThreshold = 20

    # Apply Hysteresis
    medium = np.zeros((img.shape))  # medium array for pixels between high and low threshold
    mediumW, mediumH = medium.shape

    # iterate through the filtered image and find strong and weak pixels
    for i in range(1, img.shape[0]):
        for j in range(1, img.shape[1]):
            if (img[i, j] < lowThreshold):
                img[i, j] = 0  # weak pixel
            elif (img[i, j] > highThreshold):
                img[i, j] = 1  # strong pixel
            else:
                np.append(medium, img[i, j])  # if between the high and low threshold

    isBetween = True
    while (isBetween):
        isBetween = False
        # iterate through the medium pixels array to find if pixels are connected to strong pixels
        for i in range(mediumW):
            for j in range(mediumH):
                if (medium[i, j] > 0):
                    patch = img[i:i + mediumW, j:j + mediumH]
                    if (np.sum(patch) > 0):
                        img[i, j] = 1
                        medium[i, j] = 0
                        isBetween = True
    return img


def nonMaxSuppression(img, gradOrient):
    imgWidth, imgHeight = img.shape
    suppressedImg = np.zeros((img.shape))
    p, r = 0, 0

    # Apply non-max suppression
    for i in range(1, imgWidth - 1):  # iterate through the image
        for j in range(1, imgHeight - 1):
            # horizontal; if the gradient orientation falls within this range assign the pixel values left and right of the image pixel
            if ((0 <= gradOrient[i, j] <= 22.5) or (157.5 <= gradOrient[i, j] <= 180) or (
                    -22.5 <= gradOrient[i, j] <= 0) or (-180 <= gradOrient[i, j] <= -157.5)):
                p = img[i, j + 1]
                r = img[i, j - 1]
            # diagonal 45; if the gradient orientation falls within this range assign the pixel values diagonal at a 45 degree angle of the image pixel
            elif ((22.5 <= gradOrient[i, j] < 67.5) or (-67.5 < gradOrient[i, j] <= -22.5)):
                p = img[i + 1, j - 1]
                r = img[i - 1, j + 1]
            # vertical; if the gradient orientation falls within this range assign the pixel values below and above the image pixel
            elif (67.5 <= gradOrient[i, j] < 112.5) or (-112.5 < gradOrient[i, j] <= -67.5):
                p = img[i + 1, j]
                r = img[i - 1, j]
            # diagonal 135; if the gradient orientation falls within this range assign the pixel values diagonal at a 135 degree angle of the image pixel
            elif (112.5 <= gradOrient[i, j] < 157.5) or (-157.5 < gradOrient[i, j] <= -112.5):
                p = img[i - 1, j - 1]
                r = img[i + 1, j + 1]

            # find the edge
            if (img[i, j] >= p) and (img[i, j] >= r):
                suppressedImg[i, j] = img[i, j]  # if it is an edge
            else:
                suppressedImg[i, j] = 0  # not an edge

    return suppressedImg


def canny_edge(img, sigma=3) -> (np.ndarray, np.ndarray):
    imgWidth, imgHeight = img.shape
    imgBlur = gaussianFilter(img, sigma)  # apply gaussian filter to blur image
    imgBlurGrad, gradOrient = gradientOperations(imgBlur)  # apply gradient operations and get the gradient orientation
    # cv2.imwrite("Canny Edge Canny1 s=" + str(sigma) + ".png", imgBlurGrad)

    # Apply non max suppression to blurred image
    filtImg = nonMaxSuppression(imgBlurGrad, gradOrient)

    # output the image after non-max suppression
    # cv2.imwrite("CE Suppressed s=" + str(sigma) + ".png", filtImg)

    # Apply hysteresis to non max suppressed image
    filtImg = hysteresis(filtImg)

    scalefiltImg = 255 * (filtImg / np.max(filtImg))

    # output the final canny edge image
    return scalefiltImg, filtImg


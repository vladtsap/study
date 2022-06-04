import os
from copy import deepcopy
from multiprocessing import Process

import cv2

from lab1.task1 import balance_brightness
from lab1.task2 import linear_contrasting, gamma_correction, histogram_equalisation
from utils import calculate_psnr, calculate_ssim

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_image_brightness(image, image_name):
    original_image = deepcopy(image)
    balance_brightness(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_brightness.jpg'), image)
    print(
        f'{image_name.upper()} — BRIGHTNESS | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_image_linear_contrasting(image, image_name):
    original_image = deepcopy(image)
    linear_contrasting(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_linear.jpg'), image)
    print(
        f'{image_name.upper()} — LINEAR CONTRASTING | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_image_gamma_correction(image, image_name):
    original_image = deepcopy(image)
    gamma_correction(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_gamma.jpg'), image)
    print(
        f'{image_name.upper()} — GAMMA CORRECTION | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_image_histogram_equalisation(image, image_name):
    original_image = deepcopy(image)
    histogram_equalisation(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_histogram.jpg'), image)
    print(
        f'{image_name.upper()} — HISTOGRAM EQUALIZATION | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def main():
    for root, _, files in os.walk(INPUT_PATH):
        for file in files:

            if file.startswith('.'):
                continue

            filename = file.split('.')[0]

            original_image = cv2.imread(os.path.join(root, f'{file}'))
            cv2.imwrite(os.path.join(OUTPUT_PATH, f'{filename}_original.jpg'), original_image)

            kwargs = {
                'image': original_image,
                'image_name': filename,
            }

            Process(target=process_image_brightness, kwargs=deepcopy(kwargs)).start()
            Process(target=process_image_linear_contrasting, kwargs=deepcopy(kwargs)).start()
            Process(target=process_image_gamma_correction, kwargs=deepcopy(kwargs)).start()
            Process(target=process_image_histogram_equalisation, kwargs=deepcopy(kwargs)).start()


if __name__ == '__main__':
    main()

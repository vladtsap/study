import os
from copy import deepcopy
from multiprocessing import Process

import cv2

from lab3.task1 import sobel_filter
from lab3.task2 import binarization, otsu
from lab3.task3 import k_mean
from lab3.task5 import watershed
from lab3.task4 import canny_edge
from utils import calculate_psnr, calculate_ssim

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_watershed(image, image_name, **_):
    original_image = deepcopy(image)
    image = watershed(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_watershed.jpg'), image)
    print(
        f'{image_name.upper()} — WATERSHED | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_sobel_filter(image, image_name, **_):
    original_image = deepcopy(image)
    image_x, image_y, image = sobel_filter(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_sobel_X.jpg'), image_x)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_sobel_Y.jpg'), image_y)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_sobel.jpg'), image)
    print(
        f'{image_name.upper()} — SOBEL | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_binarization(image, image_name, threshold, **_):
    original_image = deepcopy(image)
    image = binarization(image, threshold)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_binarization_{threshold}.jpg'), image)
    print(
        f'{image_name.upper()} — BINARIZATION (THRESHOLD={threshold}) | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_otsu(image, image_name, **_):
    original_image = deepcopy(image)
    image = otsu(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_otsu.jpg'), image)
    print(
        f'{image_name.upper()} — OTSU | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_canny(image, image_name, **_):
    original_image = deepcopy(image)
    image_scaled, image = canny_edge(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_canny_scaled.jpg'), image_scaled)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_canny.jpg'), image)
    print(
        f'{image_name.upper()} — OTSU | '
        f'PSNR: {round(calculate_psnr(original_image, image), 2)} | '
        f'SSIM: {round(calculate_ssim(original_image, image), 2)}'
    )


def process_k_mean(color_image, image_name, k, i, **_):
    image = color_image
    original_image = deepcopy(image)
    image = k_mean(image, k, i)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_k_mean_{k}_{i}.jpg'), image)
    print(
        f'{image_name.upper()} — K-MEAN (K={k}, I={i}) | '
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

            gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(OUTPUT_PATH, f'{filename}_gray.jpg'), gray_image)

            kwargs = {
                'image': gray_image,
                'color_image': original_image,
                'image_name': filename,
            }

            for process in [
                process_watershed,
                process_sobel_filter,
                process_otsu,
                process_canny,
            ]:
                Process(target=process, kwargs=deepcopy(kwargs)).start()

            for threshold in range(100, 180, 20):
                Process(
                    target=process_binarization,
                    kwargs=deepcopy({**kwargs, **{'threshold': threshold}}),
                ).start()

            for k in range(2, 6):
                for i in range(1, 6):
                    Process(
                        target=process_k_mean,
                        kwargs=deepcopy({**kwargs, **{'k': k, 'i': i}}),
                    ).start()


if __name__ == '__main__':
    main()

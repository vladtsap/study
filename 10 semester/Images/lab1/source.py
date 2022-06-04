import os
from copy import deepcopy
from multiprocessing import Process

import cv2

from lab1.task1 import balance_brightness
from lab1.task2 import linear_contrasting, gamma_correction, histogram_equalisation

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_image_brightness(image, image_name):
    brightness_image = balance_brightness(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_brightness.jpg'), brightness_image)
    print(f'brightness — {image_name} done')


def process_image_linear_contrasting(image, image_name):
    contrasting_image = linear_contrasting(deepcopy(image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_linear.jpg'), contrasting_image)
    print(f'linear contrasting — {image_name} done')


def process_image_gamma_correction(image, image_name):
    contrasting_image = gamma_correction(deepcopy(image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_gamma.jpg'), contrasting_image)
    print(f'gamma contrasting — {image_name} done')


def process_image_histogram_equalisation(image, image_name):
    contrasting_image = histogram_equalisation(deepcopy(image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_histogram.jpg'), contrasting_image)
    print(f'histogram histogram — {image_name} done')


if __name__ == '__main__':
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

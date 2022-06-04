import os
from copy import deepcopy
from threading import Thread

import cv2

from lab1.task1 import balance_brightness
from lab1.task2 import linear_contrasting, gamma_correction, histogram_equalisation

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_image_brightness(original_image, image_name):
    brightness_image = balance_brightness(deepcopy(original_image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_brightness.jpg'), brightness_image)
    print(f'brightness — {image_name} done')


def process_image_linear_contrasting(original_image, image_name):
    contrasting_image = linear_contrasting(deepcopy(original_image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_linear.jpg'), contrasting_image)
    print(f'linear contrasting — {image_name} done')


def process_image_gamma_correction(original_image, image_name):
    contrasting_image = gamma_correction(deepcopy(original_image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_gamma.jpg'), contrasting_image)
    print(f'gamma contrasting — {image_name} done')


def process_image_histogram_equalisation(original_image, image_name):
    contrasting_image = histogram_equalisation(deepcopy(original_image))
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting_histogram.jpg'), contrasting_image)
    print(f'histogram histogram — {image_name} done')


for root, _, files in os.walk(INPUT_PATH):
    for file in files:

        if file.startswith('.'):
            continue

        filename = file.split('.')[0]

        image = cv2.imread(os.path.join(root, f'{file}'))
        cv2.imwrite(os.path.join(OUTPUT_PATH, f'{filename}_original.jpg'), image)

        kwargs = {
            'original_image': image,
            'image_name': filename,
        }

        Thread(target=process_image_brightness, kwargs=kwargs).start()
        Thread(target=process_image_linear_contrasting, kwargs=kwargs).start()
        Thread(target=process_image_gamma_correction, kwargs=kwargs).start()
        Thread(target=process_image_histogram_equalisation, kwargs=kwargs).start()

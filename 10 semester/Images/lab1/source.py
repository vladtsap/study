import os
from threading import Thread

import cv2

from lab1.task1 import balance_brightness
from lab1.task2 import linear_contrasting

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_image_brightness(original_image, image_name):
    brightness_image = balance_brightness(original_image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_brightness.jpg'), brightness_image)
    print(f'brightness — {image_name} done')


def process_image_contrasting(original_image, image_name):
    contrasting_image = linear_contrasting(original_image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_contrasting.jpg'), contrasting_image)
    print(f'contrasting — {image_name} done')


for root, _, files in os.walk(INPUT_PATH):
    for file in files:

        if file.startswith('.'):
            continue

        filename = file.split('.')[0]

        image = cv2.imread(os.path.join(root, f'{file}'))
        cv2.imwrite(os.path.join(OUTPUT_PATH, f'{filename}_original.jpg'), image)

        Thread(
            target=process_image_brightness,
            kwargs={
                'original_image': image,
                'image_name': filename,
            },
        ).start()

        Thread(
            target=process_image_contrasting,
            kwargs={
                'original_image': image,
                'image_name': filename,
            },
        ).start()

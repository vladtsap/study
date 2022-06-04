import os
from threading import Thread

import cv2

from lab1.task1 import balance_brightness

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_image(root_path, image_name):
    original_image = cv2.imread(os.path.join(root_path, f'{image_name}.jpg'))

    brightness_image = balance_brightness(original_image)

    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_original.jpg'), original_image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_brightness.jpg'), brightness_image)

    print(f'{image_name} processed')


for root, _, files in os.walk(INPUT_PATH):
    for file in files:

        if file.startswith('.'):
            continue

        Thread(
            target=process_image,
            kwargs={
                'root_path': root,
                'image_name': file.split('.')[0],
            },
        ).start()

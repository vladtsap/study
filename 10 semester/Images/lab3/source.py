import os
from copy import deepcopy
from multiprocessing import Process

import cv2

from lab3.task5 import watershed
from utils import calculate_psnr, calculate_ssim

INPUT_PATH = 'input'
OUTPUT_PATH = 'output'


def process_watershed(image, image_name):
    original_image = deepcopy(image)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    image = watershed(image)
    cv2.imwrite(os.path.join(OUTPUT_PATH, f'{image_name}_watershed.jpg'), image)
    print(
        f'{image_name.upper()} — WATERSHED | '
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

            for process in [
                process_watershed,
            ]:
                Process(target=process, kwargs=deepcopy(kwargs)).start()


if __name__ == '__main__':
    main()

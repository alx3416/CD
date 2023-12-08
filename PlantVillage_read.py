import os
import numpy as np
import cv2

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.JPG', '.jpg']]):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                cv2.imshow("images", img)
                if cv2.waitKey(1) == 27:
                    break  # esc to quit
    return images

folders = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
]

for folder in folders:
    images = load_images_from_folder("E:/datasets/PlantVillage-Dataset/raw/color/" + folder)
    # your code that does something with the return images goes here
import os
import numpy as np
import cv2
import pandas as pd


def load_images_from_folder(path_general, folder, folders):
    y = pd.DataFrame(columns=list('Y'))
    for filename in os.listdir(path_general+folder):
        if any([filename.endswith(x) for x in ['.JPG', '.jpg']]):
            img = cv2.imread(os.path.join(path_general+folder, filename))
            if img is not None:
                y.loc[len(y.index)] = [folders.index(folder)]
                cv2.imshow("images", img)
                if cv2.waitKey(1) == 27:
                    break  # esc to quit

                # images = np.concatenate([images, img.reshape(1,-1)], axis=0)
    return y

folders = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
]
y_out = pd.DataFrame(columns=list('Y'))
for folder in folders:
    outY = load_images_from_folder("C:/data/PlantVillage-Dataset/raw/color/", folder, folders)
    y_out = pd.concat([y_out, outY])
y_out = y_out.reset_index(drop=True)
print(y_out.tail())

    # your code that does something with the return images goes here

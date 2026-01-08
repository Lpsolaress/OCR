import os
import cv2
import numpy as np

IMG_SIZE = 28

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"No se pudo leer: {img_path}")

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    img = img / 255.0
    return img

def load_dataset(base_folder):
    images = []
    labels = []

    for category in sorted(os.listdir(base_folder)):
        category_path = os.path.join(base_folder, category)
        if not os.path.isdir(category_path):
            continue

        for label in sorted(os.listdir(category_path)):
            label_path = os.path.join(category_path, label)
            if not os.path.isdir(label_path):
                continue

            for file in os.listdir(label_path):
                img_path = os.path.join(label_path, file)
                img = preprocess_image(img_path)
                images.append(img)
                labels.append(label)

    return np.array(images), np.array(labels)
import cv2
import numpy as np

IMG_SIZE = 28

def segment_characters(image):
    """
    Input: imagen binarizada (numpy array)
    Output: lista de caracteres segmentados (28x28)
    """

    # Asegurarse que es uint8
    img = (image * 255).astype(np.uint8)

    # Encontrar contornos
    contours, _ = cv2.findContours(
        img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    char_images = []
    bounding_boxes = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Filtro de ruido (muy importante)
        if w < 5 or h < 5:
            continue

        roi = img[y:y+h, x:x+w]

        # Redimensionar ROI
        roi = cv2.resize(roi, (IMG_SIZE, IMG_SIZE))

        roi = roi / 255.0

        char_images.append(roi)
        bounding_boxes.append((x, y, w, h))

    # Ordenar de izquierda a derecha
    char_images = [x for _, x in sorted(zip(bounding_boxes, char_images), key=lambda b: b[0][0])]

    return char_images


import cv2
import numpy as np

IMG_SIZE = 28

def segment_characters(image):
    img = (image * 255).astype(np.uint8)

    contours, _ = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    chars = []
    boxes = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w < 5 or h < 5:
            continue

        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (IMG_SIZE, IMG_SIZE))
        roi = roi / 255.0

        chars.append(roi)
        boxes.append((x, y))

    chars = [c for _, c in sorted(zip(boxes, chars), key=lambda b: b[0][0])]
    return chars
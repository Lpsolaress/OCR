import numpy as np

def recognize_character(char_img, dataset_X, dataset_y):
    """
    Reconoce un carácter usando correlación simple con el dataset.
    """
    best_label = None
    best_score = -1

    for i, ref_img in enumerate(dataset_X):
        score = np.sum(char_img * ref_img)  # similitud simple
        if score > best_score:
            best_score = score
            best_label = dataset_y[i]

    return best_label

def recognize_text(char_images, dataset_X, dataset_y):
    """
    Reconoce un conjunto de caracteres y devuelve el texto completo.
    """
    text = ""
    for c in char_images:
        text += recognize_character(c, dataset_X, dataset_y)
    return text

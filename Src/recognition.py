import numpy as np

def recognize_character(char_img, clf, le):
    # Aplanar la imagen del carácter para que sea compatible con el modelo
    char_img_flat = char_img.flatten().reshape(1, -1)
    
    # Predecir la etiqueta del carácter y obtener las probabilidades
    probabilities = clf.predict_proba(char_img_flat)
    predicted_label = np.argmax(probabilities)
    confidence = np.max(probabilities)
    
    # Convertir la etiqueta numérica a su representación original
    return le.inverse_transform([predicted_label])[0], confidence

def recognize_text(chars, clf, le):
    text = ""
    confidences = []
    for c in chars:
        label, confidence = recognize_character(c, clf, le)
        text += label
        confidences.append(confidence)
    # Calcular el porcentaje de confianza promedio
    avg_confidence = np.mean(confidences) * 100
    return text, avg_confidence
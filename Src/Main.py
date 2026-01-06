import os
import glob
import matplotlib.pyplot as plt

# Importar tus módulos
from preprocesamiento import load_dataset, preprocess_image, IMG_SIZE
from segmentation import segment_characters
from recognition import recognize_text

# ===============================
# 1️⃣ Cargar dataset
# ===============================
dataset_folder = "Data"
X, y = load_dataset(dataset_folder)
print(f"Total imágenes cargadas en dataset: {len(X)}")

# ===============================
# 2️⃣ Selección de imagen a reconocer
# ===============================
test_folder = "TestImages"
img_files = sorted(glob.glob(f"{test_folder}/*.*"))

if not img_files:
    raise FileNotFoundError(f"No se encontraron imágenes en {test_folder}")

print("Imágenes disponibles para reconocimiento:")
for i, f in enumerate(img_files):
    print(f"{i}: {f}")

idx = int(input(f"Selecciona el índice de la imagen a procesar (0-{len(img_files)-1}): "))
test_img_path = img_files[idx]
print("Procesando imagen:", test_img_path)

# ===============================
# 3️⃣ Cargar y preprocesar imagen de prueba
# ===============================
import cv2
img = cv2.imread(test_img_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(f"No se pudo leer la imagen: {test_img_path}")

_, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
img_bin = img_bin / 255.0

# ===============================
# 4️⃣ Segmentar caracteres
# ===============================
chars = segment_characters(img_bin)

# Mostrar caracteres segmentados
plt.figure(figsize=(10,2))
for i, c in enumerate(chars):
    plt.subplot(1, len(chars), i+1)
    plt.imshow(c, cmap='gray')
    plt.axis('off')
plt.show()

# ===============================
# 5️⃣ Reconocer texto
# ===============================
texto_reconocido = recognize_text(chars, X, y)
print("Texto reconocido:", texto_reconocido)

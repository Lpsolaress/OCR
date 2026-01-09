# 📄 Proyecto OCR en Python  
**Asignatura:** 051 – Inteligencia Artificial  
**Alumno:** Luis Pedro Solares  
**Trabajo:** Examen Final  
**Lenguaje:** Python 3  

---

## 📌 Descripción general

Este proyecto consiste en el desarrollo de un **sistema OCR (Optical Character Recognition)** implementado desde cero en Python, sin utilizar librerías externas que ya resuelvan directamente el reconocimiento de texto, como Tesseract u otros motores OCR.

El sistema es capaz de:
- Procesar imágenes externas con texto manuscrito o impreso.
- Segmentar caracteres individuales.
- Reconocer letras mayúsculas, minúsculas y números.
- Convertir el contenido de la imagen a texto digital.

El objetivo principal es comprender y aplicar los fundamentos de la **visión por computador y la inteligencia artificial**, respetando las restricciones impuestas en el enunciado del trabajo.

---

## 🎯 Objetivos del proyecto

- Implementar un OCR funcional sin usar motores OCR externos.
- Reconocer caracteres manuscritos y digitales.
- Aplicar técnicas de preprocesamiento y segmentación.
- Diseñar un sistema modular, documentado y extensible.
- Analizar las limitaciones y posibles mejoras del sistema.

---

## 📁 Estructura del proyecto


---

## 🧠 Funcionamiento del sistema

El sistema OCR se divide en cuatro fases principales:

### 1️⃣ Preprocesamiento
- Conversión de la imagen a escala de grises.
- Redimensionado a 28×28 píxeles.
- Binarización mediante umbral fijo.
- Normalización de los valores al rango [0,1].

Estas operaciones reducen el ruido y estandarizan las imágenes de entrada.

---

### 2️⃣ Segmentación
- Detección de contornos usando OpenCV.
- Eliminación de regiones pequeñas (ruido).
- Extracción de cada carácter mediante bounding boxes.
- Centrado del carácter en una imagen cuadrada.
- Redimensionado final a 28×28 píxeles.
- Ordenación de los caracteres de izquierda a derecha.

---

### 3️⃣ Reconocimiento
- Construcción de plantillas promedio por cada clase (letra o número).
- Comparación de cada carácter segmentado con dichas plantillas.
- Selección del carácter con mayor similitud usando una métrica basada en producto escalar.

Este enfoque permite un reconocimiento básico sin utilizar redes neuronales.

---

### 4️⃣ Reconstrucción del texto
Los caracteres reconocidos se concatenan en el orden correcto para obtener el texto final en formato digital.

---

## 🖼️ Imagen de entrada

La imagen `test_images/ejemplo.png` es la entrada principal del sistema.

Requisitos recomendados para obtener mejores resultados:
- Texto horizontal.
- Fondo claro y texto oscuro.
- Caracteres separados entre sí.
- Imagen en buena resolución.

---

## ▶️ Ejecución del proyecto

1. Abrir el archivo `Cuaderno.ipynb`.
2. Verificar que las carpetas `Src`, `Data` y `test_images` estén en el mismo nivel.
3. Ejecutar las celdas del notebook en orden.
4. El texto reconocido se mostrará por pantalla.

---

## 🧪 Librerías utilizadas

- Python 3
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

> No se utilizan librerías especializadas en OCR.

---

## 📊 Limitaciones conocidas

- Sensible a errores de segmentación.
- No reconoce escritura cursiva continua.
- Precisión limitada para manuscritos muy variables.
- No utiliza aprendizaje profundo.

Estas limitaciones son coherentes con el enfoque manual del proyecto.

---

## 🚀 Posibles mejoras futuras

- Uso de clasificadores KNN o redes neuronales.
- Segmentación avanzada para palabras completas.
- Reconocimiento de tablas y estructuras.
- Detección de características adicionales en imágenes.

---

## 🎓 Conclusión

Este proyecto demuestra que es posible construir un sistema OCR funcional desde cero, abordando de forma explícita cada una de las fases del proceso. Aunque no alcanza la precisión de soluciones comerciales, cumple plenamente los objetivos académicos y permite comprender en profundidad los fundamentos del reconocimiento óptico de caracteres.

---

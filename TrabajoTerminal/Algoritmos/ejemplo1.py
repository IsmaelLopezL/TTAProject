import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
import os

# Directorio donde se encuentran las imágenes de entrenamiento
training_dir = r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\training_images"

# Obtener la lista de nombres de archivos de imágenes
image_files = os.listdir(training_dir)

# Listas para almacenar imágenes y etiquetas
images = []
labels = []

# Cargar y preprocesar las imágenes de entrenamiento
for image_file in image_files:
    image_path = os.path.join(training_dir, image_file)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (128, 128))
    image = image / 255.0
    images.append(image)

    # Labels
    if "BO-" in image_file:
        label = 0  # Etiqueta 0 para "espora"
    else:
        label = 1  # Etiqueta 1 para "no espora"
    labels.append(label)

# Convertir las listas en matrices o tensores
X_train = np.array(images)
y_train = np.array(labels)

print(X_train.size)
print(y_train.size)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=8)


new_image = cv2.imread(r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\nueva_espora3.jpg")
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
new_image = cv2.resize(new_image, (128, 128))
new_image = new_image / 255.0
new_image = np.expand_dims(new_image, axis=0)

predictions = model.predict(new_image)
predicted_class = np.argmax(predictions)
print(predicted_class)



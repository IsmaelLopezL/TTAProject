import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2

# Paso 1: Preprocesar las imágenes
# Supongamos que tienes un conjunto de datos etiquetado, donde las imágenes y las etiquetas están en dos listas separadas.
# Aquí, cargamos una imagen de ejemplo y la procesamos para que tenga un tamaño fijo y se normalice.

image = cv2.imread(r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\espora.jpg")  # Reemplaza 'espora.jpg' con la ruta de tu imagen
# Display the image

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir la imagen a escala de grises

image = cv2.resize(image, (128, 128))  # Redimensionar la imagen a un tamaño fijo (ajusta según tus necesidades)
image = image / 255.0  # Normalizar los valores de píxeles al rango [0, 1]
image = np.expand_dims(image, axis=0)  # Agregar una dimensión para crear un lote (batch)

# Paso 2: Definir el modelo de la red neuronal
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128)),  # Aplanar la imagen
    keras.layers.Dense(128, activation='relu'),  # Capa oculta con activación ReLU
    keras.layers.Dense(2, activation='softmax')  # Capa de salida con dos neuronas (por ejemplo, "espora" y "no espora")
])

# Paso 3: Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Paso 4: Entrenar el modelo (suponiendo que tengas un conjunto de datos etiquetado)
# X_train contiene tus imágenes de entrenamiento y y_train las etiquetas correspondientes.
# Ajusta estos datos según tu conjunto de datos real.
X_train = image # Ejemplo con una sola imagen de entrenamiento
y_train = np.array([1])  # Suponiendo que 0 representa "espora" y 1 representa "no espora"
#print(X_train.shape)
#print(y_train.shape)

model.fit(X_train, y_train, epochs=10)  # Ajusta el número de épocas según sea necesario

# Paso 5: Hacer predicciones en nuevas imágenes
# Aquí cargamos una nueva imagen (new_image) y hacemos una predicción.
new_image = cv2.imread(r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\nueva_espora.jpg")  # Reemplaza 'nueva_espora.jpg' con la ruta de tu nueva imagen
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
new_image = cv2.resize(new_image, (128, 128))
new_image = new_image / 255.0
new_image = np.expand_dims(new_image, axis=0)

predictions = model.predict(new_image)
predicted_class = np.argmax(predictions)
print(predicted_class)
# La variable 'predicted_class' contendrá la etiqueta predicha (0 para "espora" o 1 para "no espora").

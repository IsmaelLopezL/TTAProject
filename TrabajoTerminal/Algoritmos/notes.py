
# Paso 5: Hacer predicciones en nuevas imágenes
# Aquí cargamos una nueva imagen (new_image) y hacemos una predicción.
new_image = cv2.imread(r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\nueva_espora.jpg")  # Reemplaza 'nueva_espora.jpg' con la ruta de tu nueva imagen
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
new_image = cv2.resize(new_image, (128, 128))
new_image = new_image / 255.0
new_image = np.expand_dims(new_image, axis=0)

predictions = model.predict(new_image)
predicted_class = np.argmax(predictions)

# La variable 'predicted_class' contendrá la etiqueta predicha (0 para "espora" o 1 para "no espora").






image = cv2.imread(r"C:\Users\Raderly\Documents\TrabajoTerminal\Algoritmos\espora.jpg")  # Reemplaza 'espora.jpg' con la ruta de tu imagen
# Display the image
cv2.imshow("Image", image)

# Wait for the user to press a key
cv2.waitKey(0)
 
# Close all windows
cv2.destroyAllWindows()















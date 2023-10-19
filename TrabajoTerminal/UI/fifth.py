import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
from tkinter import filedialog

def open_image(file_path):
    try:
        image = Image.open(file_path)
        max_width = 400  # Tamaño máximo deseado para el cuadro
        max_height = 400
        if image.width > max_width or image.height > max_height:
            # Reescalar la imagen si supera el tamaño máximo
            image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        label.config(width=image.width, height=image.height)  # Ajustar el tamaño del label al de la imagen
    except Exception as e:
        print("Error al abrir la imagen:", e)

def drop(event):
    file_path = event.data
    open_image(file_path)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        open_image(file_path)

def changeText():
    info_label.config(text="Tipo(s): Esporas Tipo A\nNo. de elementos diferentes: 5\nNo. Elementos en pantalla: 683\nFoto tomada con: Camara CANON X\nFecha de analisis:10/10/2023\n")


root = TkinterDnD.Tk()
root.title("Arrastrar y Abrir Imagen")
title_label = tk.Label(root, text="Analisis por NNC")
title_label.pack(padx=10, pady=(10, 5))

info_label = tk.Label(root, text="Agregue la imagenes a tratar")
info_label.pack(padx=10, pady=(40, 20),side="left")


# Crear un cuadro de diálogo a la izquierda del frame
dialog_frame = tk.Frame(root, padx=10, pady=10)
dialog_frame.pack(side="right")

label = tk.Label(root, relief="solid", width=90, height=20, borderwidth=2)
label.pack(padx=10,pady=10)

# Crear un botón en la parte inferior
buttonO = tk.Button(root, text="Abrir Imagen", command=open_file_dialog)
buttonO.pack(side="left",padx=3,pady=10)

buttonF = tk.Button(root, text="Analizar Imagen", command=changeText)
buttonF.pack(side="left",padx=3,pady=2)

buttonS = tk.Button(root, text="Guardar Datos")
buttonS.pack(side="left",padx=3,pady=2)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()

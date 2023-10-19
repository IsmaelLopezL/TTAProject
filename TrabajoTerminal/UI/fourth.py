import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

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

root = TkinterDnD.Tk()
root.title("Imagen a Tratar")

frame = tk.Frame(root)
frame.pack(padx=50, pady=10)

label = tk.Label(frame, width=200, height=40, relief="solid", borderwidth=2)
label.pack()

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
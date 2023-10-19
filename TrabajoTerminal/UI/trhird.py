import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

def open_image(file_path):
    try:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
    except Exception as e:
        print("Error al abrir la imagen:", e)

def drop(event):
    file_path = event.data
    open_image(file_path)

root = TkinterDnD.Tk()
root.title("Arrastrar y Abrir Imagen")

frame = tk.Frame(root)
frame.pack(padx=10, pady=50)

label = tk.Label(frame, width=400, height=400, relief="solid", borderwidth=2)
label.pack()

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()

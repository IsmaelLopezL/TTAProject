import customtkinter as ctk

def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("800x550")
root.title("Get Images")

title_label = ctk.CTkLabel(root, text="Agrege las imagenes a tratar", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=600, height=300)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=20)

root.mainloop()
import customtkinter as ctk
from tkinter import filedialog

# Configuración inicial
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# Crear ventana principal
root = ctk.CTk()
root.geometry("600x400")
root.title("PROFUL - Procesamiento de videos deportivos")

# Etiqueta del título principal
title_label = ctk.CTkLabel(
    root,
    text="PROFUL",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=10)

subtitle_label = ctk.CTkLabel(
    root,
    text="Procesamiento de videos deportivos",
    font=("Arial", 14)
)
subtitle_label.pack()

# Sección 1: Carga de videos
section1_label = ctk.CTkLabel(
    root,
    text="1. Carga de videos",
    font=("Arial", 18, "bold")
)
section1_label.pack(pady=10)

# Botones para seleccionar archivos
frame_videos = ctk.CTkFrame(root)
frame_videos.pack(pady=10)

video1_button = ctk.CTkButton(
    frame_videos,
    text="Seleccionar archivo",
    command=lambda: filedialog.askopenfilename()
)
video1_button.grid(row=0, column=0, padx=10, pady=5)

video2_button = ctk.CTkButton(
    frame_videos,
    text="Seleccionar archivo",
    command=lambda: filedialog.askopenfilename()
)
video2_button.grid(row=0, column=1, padx=10, pady=5)

# Etiquetas para Video 1 y Video 2
video1_label = ctk.CTkLabel(frame_videos, text="Video 1 (izquierda)")
video1_label.grid(row=1, column=0, pady=5)

video2_label = ctk.CTkLabel(frame_videos, text="Video 2 (derecha)")
video2_label.grid(row=1, column=1, pady=5)

# Sección 2: Dimensión de la cancha
section2_label = ctk.CTkLabel(
    root,
    text="2. Dimensión cancha",
    font=("Arial", 18, "bold")
)
section2_label.pack(pady=10)

frame_dimensions = ctk.CTkFrame(root)
frame_dimensions.pack(pady=10)

# Campos para alto y ancho
height_entry = ctk.CTkEntry(
    frame_dimensions,
    placeholder_text="Ingrese el alto m"
)
height_entry.grid(row=0, column=0, padx=10, pady=5)

width_entry = ctk.CTkEntry(
    frame_dimensions,
    placeholder_text="Ingrese el ancho m"
)
width_entry.grid(row=0, column=1, padx=10, pady=5)

# Botón para unir videos
unir_button = ctk.CTkButton(root, text="Unir videos", command=lambda: print("Unir videos"))
unir_button.pack(pady=20)

# Ejecutar ventana
root.mainloop()

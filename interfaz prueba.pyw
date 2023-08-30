import tkinter as tk

def mostrar_contenido(opcion):
    contenido_frame.config(text=f"Mostrando contenido de {opcion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Dividida")

# Crear un frame para los botones y el logo
botones_frame = tk.Frame(ventana)
botones_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Crear botones y logo en el frame de botones
logo = tk.Label(botones_frame, text="Logo", font=("Helvetica", 16))
logo.pack(pady=10)

boton_opcion1 = tk.Button(botones_frame, text="Agregar cliente", command=lambda: mostrar_contenido("Opción 1"))
boton_opcion1.pack(pady=5)

boton_opcion2 = tk.Button(botones_frame, text="Opción 2", command=lambda: mostrar_contenido("Opción 2"))
boton_opcion2.pack(pady=5)

# Crear un frame para mostrar el contenido
contenido_frame = tk.Label(ventana, text="", font=("Helvetica", 16))
contenido_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Iniciar la interfaz
ventana.mainloop()



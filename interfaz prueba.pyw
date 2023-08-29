import tkinter as tk

def mostrar_frame(frame):
    frame.tkraise()

# Configuración inicial de la ventana
ventana = tk.Tk()
ventana.title("Frames Visibles")
ventana.geometry("800x600")

# Crear frames
frame1 = tk.Frame(ventana, bg="blue")
frame2 = tk.Frame(ventana, bg="green")
frame3 = tk.Frame(ventana, bg="red")

# Agregar contenido a los frames
# ...

# Mostrar el primer frame por defecto
frame1.pack(fill="both", expand=True)

# Botones para cambiar entre frames
boton_frame1 = tk.Button(ventana, text="Frame 1", command=lambda: mostrar_frame(frame1))
boton_frame1.pack(side="left")

boton_frame2 = tk.Button(ventana, text="Frame 2", command=lambda: mostrar_frame(frame2))
boton_frame2.pack(side="left")

boton_frame3 = tk.Button(ventana, text="Frame 3", command=lambda: mostrar_frame(frame3))
boton_frame3.pack(side="left")

# Iniciar la aplicación
ventana.mainloop()

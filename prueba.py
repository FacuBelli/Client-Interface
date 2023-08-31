import tkinter as tk

contenido_actual = None

def mostrar_contenido1():
    global contenido_actual
    # Eliminar contenido anterior si existe
    if contenido_actual:
        contenido_actual.destroy()

    # Crear y mostrar nuevo contenido
    contenido = tk.Label(root, text="Contenido del botón 1")
    contenido.pack()
    
    contenido_actual = contenido

def mostrar_contenido2():
    global contenido_actual
    # Eliminar contenido anterior si existe
    if contenido_actual:
        contenido_actual.destroy()

    # Crear y mostrar nuevo contenido
    contenido = tk.Label(root, text="Contenido del botón 2")
    contenido.pack()
    
    contenido_actual = contenido

root = tk.Tk()


boton1 = tk.Button(root, text="Mostrar Contenido 1", command=mostrar_contenido1)
boton1.pack()

boton2 = tk.Button(root, text="Mostrar Contenido 2", command=mostrar_contenido2)
boton2.pack()

root.mainloop()

from tkinter import *

def mostrar_mensaje():
    etiqueta.config(text="¡Hola, has hecho clic!")

# Crear la ventana principal
root = Tk()
root.title("Interfaz clientes")


root.resizable(1,1) #Esto es para permitir la redimension de la ventana, son de tipo boolean y corresponden a width y height respectivamente

#root.geometry("300x200")

root.config(bg="#777")

root.iconbitmap("logo.ico")

myFrame = Frame() #A un frame hay que darle tamaño
myFrame.pack() #Hayq ue empaquetar el frame pq sino queda fuera de la raiz

myFrame.config(bg="#000")

myFrame.config(width="650", height="350", relief="groove")
myFrame.config(bd=35)


# Agregar widgets
# etiqueta = root.Label(root, text="¡Hola, bienvenido!")
# etiqueta.pack()

# boton = tk.Button(root, text="¡Haz clic!", command=mostrar_mensaje)
# boton.pack()

# Mostrar la interfaz
root.mainloop()

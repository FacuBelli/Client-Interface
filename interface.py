from tkinter import *
from database import Database
from tkinter import ttk
import pymysql

notebook = None

entry_nombre = None
entry_receta = None
entry_cristales = None
entry_orden = None
entry_armazon = None
entry_taller = None

db = None



db_config ={
    "host":  "localhost",
    "user": "root",
    "database": "optica", 
    "table": "clientes",
}

db = Database(**db_config)
db.connect()



#Espacio para agregar operaciones a la base de datos por si queremos probar algo



def agregar_cliente():
    global entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller, db
    
    nombre = entry_nombre.get()
    receta = entry_receta.get()
    cristales = entry_cristales.get()
    numero_orden = entry_orden.get()
    armazon = entry_armazon.get()
    taller = entry_taller.get()

    try:
        consulta = "INSERT INTO clientes (nombre,receta,cristales,numero_orden,armazon,taller) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor = db.get_cursor()
        cursor.execute(consulta, (nombre,receta,cristales,numero_orden,armazon,taller))

        db.connection.commit()
        print("cliente agregado correctamente")

    except Exception as e:
        print("Error al agregar el cliente: ",e)


    entry_nombre.delete(0, END)
    entry_receta.delete(0, END)
    entry_cristales.delete(0, END)
    entry_orden.delete(0, END)
    entry_armazon.delete(0, END)
    entry_taller.delete(0, END)


def mostrar_pagina_agregar_cliente():
    global notebook, db, entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller


# Crear una nueva pestaña para agregar clientes
    frame_agregar_cliente =Frame(notebook)
    notebook.add(frame_agregar_cliente, text="Agregar Cliente")

    # Etiquetas y campos de entrada para el nombre y el email
    label_nombre = Label(frame_agregar_cliente, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(frame_agregar_cliente)
    entry_nombre.pack()

    label_receta = Label(frame_agregar_cliente, text="Receta:")
    label_receta.pack()
    entry_receta = Entry(frame_agregar_cliente)
    entry_receta.pack()

    label_cristales = Label(frame_agregar_cliente, text="Cristales:")
    label_cristales.pack()
    entry_cristales = Entry(frame_agregar_cliente)
    entry_cristales.pack()

    label_orden = Label(frame_agregar_cliente, text="Número de Orden:")
    label_orden.pack()
    entry_orden = Entry(frame_agregar_cliente)
    entry_orden.pack()

    label_armazon = Label(frame_agregar_cliente, text="Armazón:")
    label_armazon.pack()
    entry_armazon = Entry(frame_agregar_cliente)
    entry_armazon.pack()

    label_taller = Label(frame_agregar_cliente, text="Taller:")
    label_taller.pack()
    entry_taller = Entry(frame_agregar_cliente)
    entry_taller.pack()


        # Botón para guardar el cliente
    boton_guardar = Button(frame_agregar_cliente, text="Guardar Cliente", command = agregar_cliente)
    boton_guardar.pack()

def mostrar_consultar_cliente():
    
    label_nombre = Label(frame_agregar_cliente, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(frame_agregar_cliente)
    entry_nombre.pack()

    cliente = entry_nombre.get()

    


    
    print("Funca")


def mostrar_editar_cliente():
    print("Holis")

root = Tk()

root.title("Interfaz clientes")
root.iconbitmap("logo.ico")


notebook = ttk.Notebook(root)


#Creando el menu
menu_principal = Menu(root)
root.config(menu = menu_principal)

#Creamos el desplegable

menu_cascade = Menu(menu_principal)
menu_principal.add_cascade(label ="Opciones", menu = menu_cascade)

menu_cascade.add_command(label="Agregar cliente", command=mostrar_pagina_agregar_cliente)
menu_cascade.add_command(label = "Consultar cliente", command = mostrar_consultar_cliente)
menu_cascade.add_command(label = "Editar cliente", command = mostrar_editar_cliente)




notebook.pack()
root.mainloop()
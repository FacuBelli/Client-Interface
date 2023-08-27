from tkinter import *
from database import Database
from tkinter import ttk
from tkinter import messagebox
import pyodbc


notebook = None

entry_nombre = None
entry_receta = None
entry_cristales = None
entry_orden = None
entry_armazon = None
entry_taller = None
entry_graduacion = None

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
    global entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller,entry_graduacion ,db
    
    nombre = entry_nombre.get()
    receta = entry_receta.get()
    cristales = entry_cristales.get()
    numero_orden = entry_orden.get()
    armazon = entry_armazon.get()
    taller = entry_taller.get()
    graduacion = entry_graduacion.get()

    try:
        consulta = "INSERT INTO clientes (nombre,receta,cristales,numero_orden,armazon,taller,graduacion) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor = db.get_cursor()
        cursor.execute(consulta, (nombre,receta,cristales,numero_orden,armazon,taller,graduacion))

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
    entry_graduacion.delete(0, END)

def consultar_cliente():
    global db , entry_nombre, notebook

    if entry_nombre:
        cliente = entry_nombre.get()

        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM clientes WHERE nombre =%s", (cliente,))

        resultado = cursor.fetchone()

        

        if resultado:
            print(resultado)
            ventana_detalle = Toplevel(root)
            ventana_detalle.title("Detalles del cliente")
            ventana_detalle.iconbitmap("logo.ico")
            ventana_detalle.resizable(1,1)

            # Mostrar los detalles del cliente en el frame
            for i, columna in enumerate(cursor.description):
                etiqueta = ttk.Label(ventana_detalle, text=columna[0] + ": ")
                etiqueta.grid(row=i, column=0, sticky="w")

                valor = ttk.Label(ventana_detalle, text=resultado[i])
                valor.grid(row=i, column=1, sticky="e")
            
       
        else:
            messagebox.showerror("Error, cliente no econtrado")
    else:
        messagebox.showerror("Error, el campo no esta definido ")






def mostrar_pagina_agregar_cliente():
    global notebook, db, entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller, entry_graduacion


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

    label_graduacion = Label(frame_agregar_cliente, text = "La receta se hizo en el local?")
    label_graduacion.pack()
    entry_graduacion = Entry(frame_agregar_cliente)
    entry_graduacion.pack()



    # Botón para guardar el cliente
    boton_guardar = Button(frame_agregar_cliente, text="Guardar Cliente", command = agregar_cliente)
    boton_guardar.pack()

def mostrar_consultar_cliente():
    global entry_nombre

    frame_consultar_cliente = Frame(notebook)
    notebook.add(frame_consultar_cliente, text="Consultar Cliente")
    
    label_nombre = Label(frame_consultar_cliente, text="Nombre:")
    label_nombre.pack()

    entry_nombre_var = StringVar()  
    entry_nombre = Entry(frame_consultar_cliente, textvariable=entry_nombre_var)
    entry_nombre.pack()

    boton_consultar = Button(frame_consultar_cliente, text="Consultar" , command=consultar_cliente)
    boton_consultar.pack()
    
#AGREGAR TIPO DE ARREGLO Y SI LA RECET FUE DEL CLIENTE O DEL LOCAL



def editar_cliente():
    editar_nombre = 0
    editar_receta = 0
    editar_cristales = 0
    editar_taller = 0
    editar_orden = 0
    editar_armazon = 0

    # update = ("UPDATE clientes SET (%s)"+ columna)

def mostrar_editar_cliente():

    global entry_nombre

    ventana_edicion = Toplevel(root)
    ventana_edicion.title("Editar cliente")
    ventana_edicion.iconbitmap("logo.ico")
    ventana_edicion.resizable(1,1)



    btn_buscar = Button(ventana_edicion, text="Buscar", command = mostrar_consultar_cliente )
    btn_buscar.pack()

    


    #Agregar una opcion que sea como quiere buscar al cliente (nombre, taller, cristales etc), con checkbox:

    busqueda_nombre = buscar_nombre.get()

    busqueda_cristales = buscar_cristales.get()


    busqueda_taller = buscar_taller.get()

    where_clause = "" #esta es la sentencia SQL WHERE
    
    # edicion_nombre = Label(ventana_edicion, text = "Nombre: ")
    # edicion_nombre.pack()
    # entry_edicion_nombre = Entry(ventana_edicion )
    # entry_edicion_nombre.pack()

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
menu_cascade.add_command(label = "Arreglos", command = "holis")


#variables de busqueda
buscar_nombre = BooleanVar()
buscar_taller = BooleanVar()
buscar_cristales = BooleanVar()

notebook.pack()
root.mainloop()
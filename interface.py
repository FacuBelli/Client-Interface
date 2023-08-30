from tkinter import *

from database import Database
from db_functions import Functions
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from tabulate import tabulate


notebook = None

entry_nombre = None
entry_receta = None
entry_cristales = None
entry_orden = None
entry_armazon = None
entry_taller = None
entry_graduacion = None

db = None

pantalla_agregar_cliente = False
pantalla_buscar_cliente = False
pantalla_editar_cliente = False

db_config ={
    "server":  "FACU\SQLEXPRESS",
    "user": "FACU\Chevrolet",
    "database": "optica", 
    "table": "clientes",
}

db = Database(**db_config)
db.connect()

funciones = Functions

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
        consulta = "INSERT INTO clientes (nombre,receta,cristales,numero_orden,armazon,taller,graduacion) VALUES (?,?,?,?,?,?,?)"
        cursor = db.get_cursor()
        cursor.execute(consulta, nombre,receta,cristales,numero_orden,armazon,taller,graduacion)

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
        cursor.execute("SELECT * FROM clientes WHERE nombre =?", (cliente,))

        resultado = cursor.fetchone()

        

        if resultado:
            print(resultado)
            ventana_detalle = Toplevel(ventana)
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
    global pantalla_agregar_cliente
    if  pantalla_agregar_cliente is False:
        crear_pagina_agregar_cliente()
        pantalla_agregar_cliente = True

def mostrar_pagina_consultar_cliente():
    global pantalla_buscar_cliente
    if pantalla_buscar_cliente is False:
        mostrar_consultar_cliente()
        pantalla_buscar_cliente = True

def mostrar_pagina_editar_cliente():
    global pantalla_editar_cliente
    if pantalla_editar_cliente is False:
        mostrar_editar_cliente()
        pantalla_editar_cliente = True   #MODIFICAR MOSTRAR_EDITAR_CLIENTE


def crear_pagina_agregar_cliente():

    global pantalla_agregar_cliente, db, entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller, entry_graduacion

    pantalla_agregar_cliente = Frame(ventana)
    pantalla_agregar_cliente.pack(side=RIGHT, padx=10, pady=10)

    label_nombre = Label(pantalla_agregar_cliente, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(pantalla_agregar_cliente)
    entry_nombre.pack()

    label_receta = Label(pantalla_agregar_cliente, text="Receta:")
    label_receta.pack()
    entry_receta = Entry(pantalla_agregar_cliente)
    entry_receta.pack()

    label_cristales = Label(pantalla_agregar_cliente, text="Cristales:")
    label_cristales.pack()
    entry_cristales = Entry(pantalla_agregar_cliente)
    entry_cristales.pack()

    label_orden = Label(pantalla_agregar_cliente, text="Número de Orden:")
    label_orden.pack()
    entry_orden = Entry(pantalla_agregar_cliente)
    entry_orden.pack()

    label_armazon = Label(pantalla_agregar_cliente, text="Armazón:")
    label_armazon.pack()
    entry_armazon = Entry(pantalla_agregar_cliente)
    entry_armazon.pack()

    label_taller = Label(pantalla_agregar_cliente, text="Taller:")
    label_taller.pack()
    entry_taller = Entry(pantalla_agregar_cliente)
    entry_taller.pack()

    label_graduacion = Label(pantalla_agregar_cliente, text = "La receta se hizo en el local?")
    label_graduacion.pack()
    entry_graduacion = Entry(pantalla_agregar_cliente)
    entry_graduacion.pack()

    boton_guardar = Button(pantalla_agregar_cliente, text="Guardar Cliente", command = agregar_cliente)
    boton_guardar.pack()

def mostrar_consultar_cliente():
    global entry_nombre

    pantalla = Frame(ventana)
    pantalla.pack(side=RIGHT, padx=10, pady=10)
    
    label_nombre = Label(pantalla, text="Nombre:")
    label_nombre.pack()

    entry_nombre_var = StringVar()  
    entry_nombre = Entry(pantalla, textvariable=entry_nombre_var)
    entry_nombre.pack()

    boton_consultar = Button(pantalla, text="Consultar" , command=consultar_cliente)
    boton_consultar.pack()
    
#AGREGAR TIPO DE ARREGLO Y SI LA RECET FUE DEL CLIENTE O DEL LOCAL



def editar_cliente():
    editar_nombre = 0
    editar_receta = 0
    editar_cristales = 0
    editar_taller = 0
    editar_orden = 0
    editar_armazon = 0

    update = ("UPDATE clientes SET (?)"+ columna)

def mostrar_editar_cliente():

    global entry_nombre

    frame_editar_cliente = Frame(notebook)
    notebook.add(frame_editar_cliente, text="Editar Cliente")

    label_nombre = Label(frame_editar_cliente, text="Nombre cliente:")
    label_nombre.pack()

    entry_nombre_var = StringVar()  
    entry_nombre = Entry(frame_editar_cliente, textvariable=entry_nombre_var)
    entry_nombre.pack()

    btn_buscar = Button(frame_editar_cliente, text="Buscar", command = consultar_cliente )
    btn_buscar.pack()


    busqueda_nombre = buscar_nombre.get()


    where_clause = "" #esta es la sentencia SQL WHERE
    





def mostrar_base():

    cursor = db.get_cursor()

    if cursor:
        cursor.execute("SELECT * FROM clientes")
        results = cursor.fetchall()

        ventana_resultados = Toplevel(root)
        ventana_resultados.title("Resultados de la Base de Datos")

        resultados_text = Text(ventana_resultados)
        
        resultados_text.pack()

        headers = [column[0] for column in cursor.description]
        formatted_results = tabulate(results, headers, tablefmt="flex")

        resultados_text.insert(END, formatted_results)

        cursor.close()  # Cierra el cursor


# Crear la ventana principal
ventana = Tk()
ventana.title("Centro Optico Illodo - Clientes")
ventana.geometry("500x500")

pantalla = Frame(ventana)
pantalla.pack(side = TOP )

# Crear un frame para los botones y el logo
botones_frame = Frame(ventana)
botones_frame.pack(side=LEFT, padx=10, pady=10)

# Crear botones y logo en el frame de botones
logo = Label(botones_frame, text="Logo", font=("Helvetica", 16))
logo.pack(pady=10)

boton_agregar_cliente = Button(botones_frame, text="Agregar cliente", command=mostrar_pagina_agregar_cliente)
boton_agregar_cliente.pack(pady=5)

boton_consulta_cliente = Button(botones_frame, text="Consultar cliente", command=mostrar_pagina_consultar_cliente)
boton_consulta_cliente.pack(pady=5)

boton_editar_cliente = Button(botones_frame, text="Editar cliente", command=mostrar_pagina_editar_cliente)
boton_editar_cliente.pack(pady=5)

# Crear un frame para mostrar el contenido
contenido_frame = Label(ventana, text="", font=("Helvetica", 16))
contenido_frame.pack(side=RIGHT, padx=10, pady=10)



# Iniciar la interfaz
ventana.mainloop()


"""root = Tk()

root.title("Interfaz clientes")
root.iconbitmap("logo.ico")"""

"""
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
menu_cascade.add_command(label = "base de datos", command = mostrar_base)



#variables de busqueda
buscar_nombre = BooleanVar()
buscar_taller = BooleanVar()
buscar_cristales = BooleanVar()

notebook.pack()
root.mainloop()"""
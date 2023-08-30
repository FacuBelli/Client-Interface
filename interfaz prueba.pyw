from tkinter import *

from database import Database

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

info = None


db_config ={
    "server":  "FACU\SQLEXPRESS",
    "user": "FACU\Chevrolet",
    "database": "optica", 
    "table": "clientes",
}

db = Database(**db_config)
db.connect()

def eliminar_cliente():
    global db
    id = info.selection()[0]
    if int(id) > 0:
        query = "DELETE FROM clientes WHERE id="+id
        db.cursor.execute(query)
        db.connection.commit()

        info.delete(id)

def mostrar_base(): #Aun no anda
    global info

    txtmessage = Label(marco, text = "Mensajes", fg="green").grid(column= 0, row = 6, columnspan=7)
    
    info = ttk.Treeview(marco)
    info.grid(column= 0, row = 8, columnspan=8, padx=15)
    info["columns"] = ("Nombre","Receta","Cristales","Orden N°", "Armazon", "Taller", "Graduacion")
    info.column("#0",width = 0,  stretch= NO)
    info.column("Nombre",width = 100,  anchor= CENTER)
    info.column("Receta",width = 250, anchor = CENTER)
    info.column("Cristales",width = 100, anchor = CENTER)
    info.column("Orden N°",width = 100, anchor = CENTER)
    info.column("Armazon",width = 100, anchor = CENTER)
    info.column("Taller",width = 100, anchor = CENTER)
    info.column("Graduacion",width = 100, anchor = CENTER)

    info.heading("Nombre",text = "Nombre", anchor = CENTER)
    info.heading("Receta",text = "Receta", anchor = CENTER)
    info.heading("Cristales",text = "Cristales", anchor = CENTER)
    info.heading("Orden N°",text = "Orden N°", anchor = CENTER)
    info.heading("Armazon",text = "Armazon", anchor = CENTER)
    info.heading("Taller",text = "Taller", anchor = CENTER)
    info.heading("Graduacion",text =" Graduacion", anchor = CENTER)


    cursor = db.get_cursor()

 
    cursor.execute("SELECT * FROM clientes")
    results = cursor.fetchall()

    for fila in results:
        id_cliente = fila[0]
        formatted_values = [str(val) for val in fila[0:]]  # Convierte los valores en cadenas
        
    # Asegúrate de que el ID del cliente no esté ya en el Treeview
        if not info.exists(id_cliente):
            info.insert("", END, id_cliente, text=id_cliente, values=formatted_values)
        else:
            print(f"El ID {id_cliente} ya existe en el Treeview")

ventana = Tk()
ventana.title("Centro Optico Illodo - Clientes")
ventana.geometry("1000x1000")
ventana.iconbitmap("logoICO.ico")

marco = LabelFrame(ventana)
marco.place(x = 50, y = 50, width = 900, height = 400)


boton_agregar_cliente = Button(marco, text="Agregar cliente ") #command=mostrar_pagina_agregar_cliente)
boton_agregar_cliente.grid(column = 1, row=1,padx=30)

boton_consulta_cliente = Button(marco, text="Consultar cliente") #command=mostrar_pagina_consultar_cliente)
boton_consulta_cliente.grid(column=2,row=1,padx=20)

boton_editar_cliente = Button(marco, text="Editar cliente ") #command=mostrar_pagina_editar_cliente)
boton_editar_cliente.grid(column=3, row = 1,padx=20)

boton_eliminar_cliente = Button(marco, text="Eliminar cliente ") #command=mostrar_pagina_editar_cliente)
boton_eliminar_cliente.grid(column=4, row = 1,padx=20)

boton_mostrar_base = Button(marco, text="Ver base de datos", command=mostrar_base)
boton_mostrar_base.grid(column=5, row = 1,padx=20, pady=10 )







ventana.mainloop()
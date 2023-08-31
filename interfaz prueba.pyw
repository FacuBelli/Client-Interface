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

contenido_actual = None





db_config ={
    "server":  "FACU\SQLEXPRESS",
    "user": "FACU\Chevrolet",
    "database": "optica", 
    "table": "clientes",
}

db = Database(**db_config)
cursor = db.get_cursor
db.connect()



def mostrar_pagina_agregar_cliente():
    pantalla_agregar_cliente = False
    if  pantalla_agregar_cliente is False:
        mostrar_agregar_cliente()
        pantalla_agregar_cliente = True

def mostrar_pagina_consultar_cliente():
    pantalla_consulta = False
    if pantalla_consulta is False:
        mostrar_consultar_cliente()
        pantalla_consulta = True

def mostrar_pagina_editar_cliente():
    pantalla_editar_cliente = False
    if pantalla_editar_cliente is False:
        mostrar_editar_cliente()
        pantalla_editar_cliente = True        

def ver_base():
    info = False
    if info is False:
        mostrar_base()
        info = True



def mostrar_base():
    global db, contenido_actual


    if contenido_actual != None:
        contenido_actual.destroy()
    
    

    info = ttk.Treeview(marco)
    info.grid(column= 0, row = 8, columnspan=8, padx=15)

    contenido_actual = info

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

    contenido_actual = info


    cursor = db.get_cursor()

    cursor.execute("SELECT * FROM clientes")
    results = cursor.fetchall()

    for fila in results:
        id_cliente = fila[7]
        formatted_values = [str(val) for val in fila[0:]]  # Convierte los valores en cadenas
        info.insert("", END, id_cliente, text=id_cliente, values=formatted_values)
    
    

    def eliminar_cliente():
        global db, cursor

        selected_item = info.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione el registro a eliminar.")
            return

        item_id = selected_item[0]
        item_nombre = info.item(item_id, "text")
        try:
            query = f"DELETE FROM clientes WHERE id_cliente='{item_nombre}'"
            cursor = db.get_cursor()
            cursor.execute(query)
            
            db.connection.commit()
            info.delete(item_id)
            

            txtmessage = Label(marco, text = "Cliente eliminado con exito", fg="green").grid(column= 0, row = 6, columnspan=7)
        except Exception as e:
            txtmessage = Label(marco, text = "Seleccione el registro a eliminar", fg="green").grid(column= 0, row = 6, columnspan=7)
            print("Error: ",e)
        
    boton_eliminar_cliente = Button(marco, text="Eliminar cliente ", command=eliminar_cliente)
    boton_eliminar_cliente.grid(column=4, row = 1,padx=40)

def agregar_cliente():
    global db,entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller,entry_graduacion
    
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
        
        txtmessage = Label(marco, text = "Cliente agregado con exito", fg="green").grid(column= 0, row = 15, columnspan=7)
        

    except Exception as e:
        print("Error al agregar el cliente: ",e)


    entry_nombre.delete(0, END)
    entry_receta.delete(0, END)
    entry_cristales.delete(0, END)
    entry_orden.delete(0, END)
    entry_armazon.delete(0, END)
    entry_taller.delete(0, END)
    entry_graduacion.delete(0, END)


def mostrar_agregar_cliente():

    global entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller,entry_graduacion, contenido_actual

    #Chequeamos que no haya otra ventana abierta, en ese caso la cerramos

    if contenido_actual != None:
        contenido_actual.destroy()
    

    pantalla_agregar_cliente = Frame(ventana)
    pantalla_agregar_cliente.pack(side=TOP, padx=50, pady=100)

    contenido_actual = pantalla_agregar_cliente

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
    boton_guardar.pack(pady = 15)


def mostrar_consultar_cliente():
    global entry_nombre, contenido_actual

    if contenido_actual != None:
        contenido_actual.destroy()

    pantalla_consulta = Frame(ventana)
    pantalla_consulta.pack(side=TOP, padx=50, pady=100)

    contenido_actual = pantalla_consulta
    
    label_nombre = Label(pantalla_consulta, text="Nombre del cliente:")
    label_nombre.pack()

    entry_nombre_var = StringVar()  
    entry_nombre = Entry(pantalla_consulta, textvariable=entry_nombre_var)
    entry_nombre.pack()

    boton_consultar = Button(pantalla_consulta, text="Consultar" , command=consultar_cliente)
    boton_consultar.pack()

def consultar_cliente():
    global db , entry_nombre

    if entry_nombre:
        cliente = entry_nombre.get()

        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM clientes WHERE nombre =?", (cliente,))

        resultado = cursor.fetchone()

        

        if resultado:
            print(resultado)
            ventana_detalle = Frame(ventana)
            ventana_detalle.configure(bg = "#fff")
            ventana_detalle.pack(side=TOP, padx=50)
            

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




    
ventana = Tk()
ventana.title("Centro Optico Illodo - Clientes")
ventana.geometry("1000x1000")
ventana.iconbitmap("logoICO.ico")

marco = LabelFrame(ventana)
marco.place(x = 50, y = 50, width = 900, height = 400)


boton_agregar_cliente = Button(marco, text="Agregar cliente ", command=mostrar_pagina_agregar_cliente)
boton_agregar_cliente.grid(column = 1, row=1,padx=40)

boton_consulta_cliente = Button(marco, text="Consultar cliente", command=mostrar_pagina_consultar_cliente)
boton_consulta_cliente.grid(column=2,row=1,padx=40)

boton_editar_cliente = Button(marco, text="Editar cliente ") #command=mostrar_pagina_editar_cliente)
boton_editar_cliente.grid(column=3, row = 1,padx=40)



boton_mostrar_base = Button(marco, text="Ver base de datos", command=mostrar_base)
boton_mostrar_base.grid(column=5, row = 1,padx=40, pady=10 )







ventana.mainloop()
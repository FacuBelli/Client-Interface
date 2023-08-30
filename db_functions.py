
class Functions:
    def __init__(self,db):
        self.db = db
    
    def agregar_cliente(self, entry_nombre, entry_receta, entry_cristales, entry_orden, entry_armazon, entry_taller, entry_graduacion):
        self.nombre = entry_nombre.get()
        self.receta = entry_receta.get()
        self.cristales = entry_cristales.get()
        self.numero_orden = entry_orden.get()
        self.armazon = entry_armazon.get()
        self.taller = entry_taller.get()
        self.graduacion = entry_graduacion.get()

        try:
            consulta = "INSERT INTO clientes (nombre, receta, cristales, numero_orden, armazon, taller, graduacion) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor = self.db.get_cursor()
            cursor.execute(consulta, (nombre, receta, cristales, numero_orden, armazon, taller, graduacion))

            self.db.connection.commit()
            print("Cliente agregado correctamente")

        except Exception as e:
            print("Error al agregar el cliente:", e)

        entry_nombre.delete(0, END)
        entry_receta.delete(0, END)
        entry_cristales.delete(0, END)
        entry_orden.delete(0, END)
        entry_armazon.delete(0, END)
        entry_taller.delete(0, END)
        entry_graduacion.delete(0, END)

    def mostrar_pagina_agregar_cliente(self,notebook,db,entry_nombre,entry_receta,entry_cristales, entry_orden, entry_armazon, entry_taller, entry_graduacion):


        pantalla = Frame(ventana)
        pantalla.pack(side=RIGHT, padx=10, pady=10)

        label_nombre = Label(pantalla, text="Nombre:")
        label_nombre.pack()
        entry_nombre = Entry(pantalla)
        entry_nombre.pack()

        label_receta = Label(pantalla, text="Receta:")
        label_receta.pack()
        entry_receta = Entry(pantalla)
        entry_receta.pack()

        label_cristales = Label(pantalla, text="Cristales:")
        label_cristales.pack()
        entry_cristales = Entry(pantalla)
        entry_cristales.pack()

        label_orden = Label(pantalla, text="Número de Orden:")
        label_orden.pack()
        entry_orden = Entry(pantalla)
        entry_orden.pack()

        label_armazon = Label(pantalla, text="Armazón:")
        label_armazon.pack()
        entry_armazon = Entry(pantalla)
        entry_armazon.pack()

        label_taller = Label(pantalla, text="Taller:")
        label_taller.pack()
        entry_taller = Entry(pantalla)
        entry_taller.pack()

        label_graduacion = Label(pantalla, text = "La receta se hizo en el local?")
        label_graduacion.pack()
        entry_graduacion = Entry(pantalla)
        entry_graduacion.pack()

        boton_guardar = Button(pantalla, text="Guardar Cliente", command = agregar_cliente)
        boton_guardar.pack()

    def consultar_cliente(self, entry_nombre, ventana):
        cliente = entry_nombre.get()

        if cliente:
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM clientes WHERE nombre = ?", (cliente,))
            resultado = cursor.fetchone()

            if resultado:
                print(resultado)
                ventana_detalle = Toplevel(ventana)
                ventana_detalle.title("Detalles del cliente")
                ventana_detalle.resizable(1, 1)

                for i, columna in enumerate(cursor.description):
                    etiqueta = ttk.Label(ventana_detalle, text=columna[0] + ": ")
                    etiqueta.grid(row=i, column=0, sticky="w")

                    valor = ttk.Label(ventana_detalle, text=resultado[i])
                    valor.grid(row=i, column=1, sticky="e")

            else:
                messagebox.showerror("Error", "Cliente no encontrado")
        else:
            messagebox.showerror("Error", "Campo no definido")
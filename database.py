import pyodbc


class Database:
    def __init__(self,server,user,database,table):
        self.server = server
        self.user = user
        self.database = database
        self.table = table
        self.connection = None

    def connect(self):
        try:
            connection_string = f'DRIVER=SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.user}; Trusted_Connection=yes;'
            self.connection = pyodbc.connect(connection_string)
            

            print("Se conecto correctamente")

        except pyodbc.Error as e:
            print("Error al conectar a la base de datos: ",e)
    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def select_table(self,table_name):
        self.table_name = table_name

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            print("No hay conexion a la base de datos")
            return None
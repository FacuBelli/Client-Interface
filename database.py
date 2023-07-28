import pymysql




class Database:
    def __init__(self,host,user,database,table):
        self.host = host
        self.user = user
        self.database = database
        self.table = table
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host = self.host,
            user = self.user,
            database = self.database,
        )

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
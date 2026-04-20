import mysql.connector

class Conexion:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'finanzas'
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
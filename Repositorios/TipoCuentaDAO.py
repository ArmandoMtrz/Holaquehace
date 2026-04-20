from Entidades.TipoCuenta import TipoCuenta

class TipoCuentaDAO:

    def __init__(self, db_connection):
        """
        Inicializa el DAO de TipoCuenta.
        :param db_connection: Un objeto de conexión a la base de datos ya establecido.
        """
        self.db_connection = db_connection

    def insertar(self, data: TipoCuenta):
        """
        Prepara una consulta de inserción para un TipoCuenta.
        No ejecuta commit ni cierra la conexión.
        """
        cursor = self.db_connection.cursor()
        try:
            query = "INSERT INTO tipoCuenta (idTipoCuenta, tipoCuenta, categoria, subcategoria) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, data.to_params(es_update=False))
            print("Consulta de inserción para TipoCuenta ejecutada.")
        finally:
            cursor.close()

    def actualizar(self, data: TipoCuenta):
        """
        Prepara una consulta de actualización para un TipoCuenta.
        No ejecuta commit ni cierra la conexión.
        """
        cursor = self.db_connection.cursor()
        try:
            query = "UPDATE tipoCuenta SET tipoCuenta = %s, categoria = %s, subcategoria = %s WHERE idTipoCuenta = %s"
            cursor.execute(query, data.to_params(es_update=True))
            print("Consulta de actualización para TipoCuenta ejecutada.")
        finally:
            cursor.close()

    def buscarPorId(self, idTipoCuenta: int):
        """
        Busca un TipoCuenta por su ID.
        """
        cursor = self.db_connection.cursor()
        try:
            query = "SELECT * FROM tipoCuenta WHERE idTipoCuenta = %s"
            cursor.execute(query, (idTipoCuenta,))
            row = cursor.fetchone()
            return TipoCuenta.from_row(row)
        finally:
            cursor.close()

from Entidades.LibroMayor import LibroMayor
from decimal import Decimal

#Finalmente mande a la chingada a Copilot xD
#La desactive y justo despues de eso me di cuenta de un par de errores en los otros 5 DAO que "hice"
#Ironias de la vida  ¯\_( ͡❛ ͜ʖ ͡❛)_/¯

class LibroMayorDAO:

    def __init__(self, Conexion):
        self.conexion = Conexion

    def insertar(self, data: LibroMayor):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO libroMayor (folioMayor, periodo, saldo, cuenta) VALUE (%s, %s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Folio mayor insertado existosamente")
            except Exception as e:
                print(f"Error al insertar el folio mayor: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")

    def actualizar(self, data: LibroMayor):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE libroMayor SET periodo = %s, saldo = %s, cuenta = %s WHERE folioMayor = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Folio mayor actualizado existosamente")
            except Exception as e:
                print(f"Error al actualizar el folio mayor: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")

    def listar(self):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayor"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [LibroMayor.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los folios mayores: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
        
    def buscarPorId(self, folioMayor: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayor WHERE folioMayor = %s"
                cursor.execute(query, (folioMayor,))
                row = cursor.fetchone()
                return LibroMayor.from_row(row)
            except Exception as e:
                print(f"Error al buscar el folio mayor por ID: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return None
        
    #operador puede ser >, <, >=, <=, =, !=
    def buscarPorCriterioSaldo(self, operador: str, saldo: Decimal):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = f"SELECT * FROM libroMayor WHERE saldo {operador} %s"
                cursor.execute(query, (saldo,))
                rows = cursor.fetchall()
                return [LibroMayor.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los folios mayores por saldo: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []

    def buscarPorCuenta(self, cuenta: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayor WHERE cuenta = %s"
                cursor.execute(query, (cuenta,))
                rows = cursor.fetchall()
                return [LibroMayor.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los folios mayores por cuenta: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
        
    def buscarPorPeriodo(self, periodo: str):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayor WHERE periodo = %s"
                cursor.execute(query, (periodo,))
                rows = cursor.fetchall()
                return [LibroMayor.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los folios mayores por periodo: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
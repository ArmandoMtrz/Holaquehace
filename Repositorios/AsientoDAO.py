from Entidades.Asiento import Asiento
from decimal import Decimal


#Aca yo namas ejerci como supervisor xD
#Namas pense en todos los posibles metodos y le di tab al escribir el nombre de la funcion
#Maldito VSC me hace sentir idiota
#Me wa a robar la chamba que no tengo xD


class AsientoDAO:
    
    def __init__(self, Conexion):
        self.conexion = Conexion()

    def insertar(self, data: Asiento):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO asiento (idAsiento, fecha, concepto, debe, haber, tipoAsiento) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Asiento insertado correctamente.")
            except Exception as e:
                print(f"Error al insertar el asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def actualizar(self, data: Asiento):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE asiento SET fecha = %s, concepto = %s, debe = %s, haber = %s, tipoAsiento = %s WHERE idAsiento = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Asiento actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar el asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")    

    def buscarPorId(self, idAsiento: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asiento WHERE idAsiento = %s"
                cursor.execute(query, (idAsiento,))
                row = cursor.fetchone()
                return Asiento.from_row(row)
            except Exception as e:
                print(f"Error al buscar el asiento por ID: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return None
        
    def listar(self):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asiento"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los asientos: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorTipoAsiento(self, idTipoAsiento: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asiento WHERE tipoAsiento = %s"
                cursor.execute(query, (idTipoAsiento,))
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los asientos por tipo de asiento: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorFecha(self, fecha: str):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asiento WHERE fecha = %s"
                cursor.execute(query, (fecha,))
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los asientos por fecha: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorConcepto(self, concepto: str):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asiento WHERE concepto LIKE %s"
                cursor.execute(query, (f"%{concepto}%",))
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los asientos por concepto: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def eliminar(self, idAsiento: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "DELETE FROM asiento WHERE idAsiento = %s"
                cursor.execute(query, (idAsiento,))
                acceso.commit()
                print("Asiento eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar el asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    #Funciona para debe o haber dependiendo del string otorgado
    def buscarPorMontoMenorOIgualA(self, debe_o_haber: str, monto: Decimal):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = f"SELECT * FROM asiento WHERE {debe_o_haber} <= %s"
                cursor.execute(query, (monto,))
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los datos por monto en {debe_o_haber}")
                return []
            finally:
                cursor.close()
        else:
            print(f"No se pudo establecer la conexion a la base de datos")
            return []
        
    #Funciona para debe o haber dependiendo del string otorgado
    #Operador debe de ser >= o <= como string
    #Cuatro metodos con 4 queries diferentes, todo unificado en uno solo
    #Soy la mamada kbron wooooooooooooooooooooooooooooooooooooo
    def buscarPorCriterioDeMonto(self, debe_o_haber: str, operador: str , monto: Decimal):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = f"SELECT * FROM asiento WHERE {debe_o_haber} {operador} %s"
                cursor.execute(query, (monto,))
                rows = cursor.fetchall()
                return [Asiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los datos por monto en {debe_o_haber}: {e}")
                return []
            finally:
                cursor.close()
        else:
            print(f"No se pudo establecer la conexion a la base de datos")
            return []
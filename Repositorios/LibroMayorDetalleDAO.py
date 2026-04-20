from Entidades.LibroMayorDetalle import LibroMayorDetalle
from decimal import Decimal

class LibroMayorDetalleDAO:

    def __init__(self, Conexion):
        self.conexion = Conexion

    def insertar(self, data: LibroMayorDetalle):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO libroMayorDetalle (debe, haber, folioMayor) VALUE (%s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Detalle de libro mayor insertado existosamente")
            except Exception as e:
                print(f"Error al insertar el detalle de libro mayor: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")

    def actualizar(self, data: LibroMayorDetalle):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE libroMayorDetalle SET debe = %s, haber = %s, folioMayor = %s WHERE idDetalleLMD = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Detalle de libro mayor actualizado existosamente")
            except Exception as e:
                print(f"Error al actualizar el detalle de libro mayor: {e}")
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
                query = "SELECT * FROM libroMayorDetalle"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [LibroMayorDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los detalles de libro mayor: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
        
    def buscarPorId(self, idDetalleLMD: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayorDetalle WHERE idDetalleLMD = %s"
                cursor.execute(query, (idDetalleLMD,))
                row = cursor.fetchone()
                return LibroMayorDetalle.from_row(row)
            except Exception as e:
                print(f"Error al buscar el detalle de libro mayor por ID: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return None
        
    def buscarPorFolioMayor(self, folioMayor: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM libroMayorDetalle WHERE folioMayor = %s"
                cursor.execute(query, (folioMayor,))
                rows = cursor.fetchall()
                return [LibroMayorDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los detalles de libro mayor por folio mayor: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
        
    #Busqueda maestra para buscar por debe o haber, operador puede ser >, <, >=, <=, =, !=
    def buscarPorCriterioDebeHaber(self, debeOHaber: str, operador: str, monto: Decimal):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = f"SELECT * FROM libroMayorDetalle WHERE {debeOHaber} {operador} %s"
                cursor.execute(query, (monto, monto))
                rows = cursor.fetchall()
                return [LibroMayorDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los detalles de libro mayor por criterio de debe/haber: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
            return []
    
    def eliminar(self, idDetalleLMD: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "DELETE FROM libroMayorDetalle WHERE idDetalleLMD = %s"
                cursor.execute(query, (idDetalleLMD,))
                acceso.commit()
                print("Detalle de libro mayor eliminado existosamente")
            except Exception as e:
                print(f"Error al eliminar el detalle de libro mayor: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("Error al establecer la conexion a la base de datos")
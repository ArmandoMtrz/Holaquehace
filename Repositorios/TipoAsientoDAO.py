from Entidades.TipoAsiento import TipoAsiento

#Mañana desactivo esta monda y me pongo a chambear por mi mismo
#Sino me va a doler el culo y no wa haber hecho mas que pulsae una tecla xD
#Esta wea tendra mas bugs que Microslop

class TipoAsientoDAO:

    def __init__(self, Conexion):
        self.conexion = Conexion()

    def insertar(self, data: TipoAsiento):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO tipoAsiento (idTipoAsiento, tipoAsiento) VALUES (%s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Tipo de asiento insertado correctamente.")
            except Exception as e:
                print(f"Error al insertar el tipo de asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def actualizar(self, data: TipoAsiento):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE tipoAsiento SET tipoAsiento = %s WHERE idTipoAsiento = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Tipo de asiento actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar el tipo de asiento: {e}")
                acceso.rollback()
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
                query = "SELECT * FROM tipoAsiento"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [TipoAsiento.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los tipos de asiento: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def eliminar(self, idTipoAsiento: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "DELETE FROM tipoAsiento WHERE idTipoAsiento = %s"
                cursor.execute(query, (idTipoAsiento,))
                acceso.commit()
                print("Tipo de asiento eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar el tipo de asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
from Entidades.AsientoDetalle import AsientoDetalle

#Re aburrido programar asi con la ia XD
#Pero me da hueva buscar como desactivarlo

class AsientoDetalleDAO:
    
    def __init__(self, Conexion):
        self.conexion = Conexion()

    def insertar(self, data: AsientoDetalle):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO asientoDetalle (idDetalleA, cuenta, debe, haber, asiento) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Detalle de asiento insertado correctamente.")
            except Exception as e:
                print(f"Error al insertar el detalle de asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def actualizar(self, data: AsientoDetalle):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE asientoDetalle SET cuenta = %s, debe = %s, haber = %s , asiento = %s WHERE idDetalleA = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Detalle de asiento actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar el detalle de asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def buscarPorId(self, idDetalleA: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asientoDetalle WHERE idDetalleA = %s"
                cursor.execute(query, (idDetalleA,))
                row = cursor.fetchone()
                return AsientoDetalle.from_row(row)
            except Exception as e:
                print(f"Error al buscar el detalle de asiento por ID: {e}")
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
                query = "SELECT * FROM asientoDetalle"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [AsientoDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar los detalles de asiento: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorAsiento(self, idAsiento: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asientoDetalle WHERE asiento = %s"
                cursor.execute(query, (idAsiento,))
                rows = cursor.fetchall()
                return [AsientoDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los detalles de asiento por ID de asiento: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorCuenta(self, idCuenta: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM asientoDetalle WHERE cuenta = %s"
                cursor.execute(query, (idCuenta,))
                rows = cursor.fetchall()
                return [AsientoDetalle.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al buscar los detalles de asiento por ID de cuenta: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def eliminar(self, idDetalleA: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "DELETE FROM asientoDetalle WHERE idDetalleA = %s"
                cursor.execute(query, (idDetalleA,))
                acceso.commit()
                print("Detalle de asiento eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar el detalle de asiento: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
from Entidades.TipoCuenta import TipoCuenta

#Creo que ya se esta enojando la ia de esta monda
#Ya no me da completas algunas funciones al darle tab
#Y encima ya no me sugiere comentarios como antes

class TipoCuentaDAO:

    def __init__(self, Conexion):
        self.conexion = Conexion

    def insertar(self, data: TipoCuenta):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO tipoCuenta (idTipoCuenta, tipoCuenta, categoria, subcategoria) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Tipo de cuenta insertado correctamente.")
            except Exception as e:
                print(f"Error al insertar el tipo de cuenta: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def actualizar(self, data: TipoCuenta):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE tipoCuenta SET tipoCuenta = %s, categoria = %s, subcategoria = %s WHERE idTipoCuenta = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Tipo de cuenta actualizado correctamente.")
            except Exception as e:
                print(f"Error al actualizar el tipo de cuenta: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return None

    def buscarPorId(self, idTipoCuenta: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM tipoCuenta WHERE idTipoCuenta = %s"
                cursor.execute(query, (idTipoCuenta,))
                row = cursor.fetchone()
                return TipoCuenta.from_row(row)
            except Exception as e:
                print(f"Error al buscar el tipo de cuenta por ID: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return None
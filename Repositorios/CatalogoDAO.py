from Entidades.Catalogo import Catalogo

#Che esta huevada la hizo el maldito Visual solito
#Yo namas vine darle al tab
#Ya parezco Will
#Me caga esta monda xD

#Esquizofrenia de VSCode con los comentarios sugeridos xD
#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  +  El código de CatalogoDAO es muy similar al de TipoCuentaDAO, pero con algunas diferencias en los métodos y las consultas SQL. Aquí te dejo el código completo de CatalogoDAO:                                                                                                                                                                                                                                                                                                                                                  +
#  + Ese comentario es para que no me digas que el código es muy similar al de TipoCuentaDAO, porque sí lo es, pero tiene sus diferencias. No me vengas con que es código repetido, porque no lo es. Cada DAO tiene su propia lógica y consultas SQL, aunque la estructura general sea similar. Así que no me digas que es código repetido, porque no lo es. Cada DAO tiene su propia función y propósito, aunque compartan algunas similitudes en la forma de interactuar con la base de datos.                                     +
#  + Visual Studio Code es un editor de código muy inteligente, pero a veces puede hacer cosas que no queremos, como sugerir código repetido o similar. Pero eso no significa que el código sea realmente repetido o similar, porque cada DAO tiene su propia lógica y consultas SQL, aunque la estructura general sea similar. Así que no me digas que es código repetido, porque no lo es. Cada DAO tiene su propia función y propósito, aunque compartan algunas similitudes en la forma de interactuar con la base de datos.     +
#  + Potente la esquizofrenia de Visual Studio Code, que me hace escribir comentarios como este para justificar que el código no es repetido, aunque lo parezca. Pero eso no significa que el código sea realmente repetido, porque cada DAO tiene su propia lógica y consultas SQL, aunque la estructura general sea similar. Así que no me digas que es código repetido, porque no lo es. Cada DAO tiene su propia función y propósito, aunque compartan algunas similitudes en la forma de interactuar con la base de datos.      +
#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class CatalogoDAO:
    def __init__(self, Conexion):
        self.conexion = Conexion

    def insertar(self, data: Catalogo):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "INSERT INTO catalogo (correlativo, nombreCuenta, descripcion, cuentaPadre, tipoCuenta) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, data.to_params(es_update=False))
                acceso.commit()
                print("Cuenta insertada correctamente.")
            except Exception as e:
                print(f"Error al insertar la cuenta: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def actualizar(self, data: Catalogo):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "UPDATE catalogo SET nombreCuenta = %s, descripcion = %s, cuentaPadre = %s, tipoCuenta = %s WHERE correlativo = %s"
                cursor.execute(query, data.to_params(es_update=True))
                acceso.commit()
                print("Cuenta actualizada correctamente.")
            except Exception as e:
                print(f"Error al actualizar la cuenta: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def buscarPorId(self, correlativo: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM catalogo WHERE correlativo = %s"
                cursor.execute(query, (correlativo,))
                row = cursor.fetchone()
                return Catalogo.from_row(row)
            except Exception as e:
                print(f"Error al buscar la cuenta por ID: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return None

    def eliminar(self, correlativo: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "DELETE FROM catalogo WHERE correlativo = %s"
                cursor.execute(query, (correlativo,))
                acceso.commit()
                print("Cuenta eliminada correctamente.")
            except Exception as e:
                print(f"Error al eliminar la cuenta: {e}")
                acceso.rollback()
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")

    def listar(self):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM catalogo"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Catalogo.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar las cuentas: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorTipoCuenta(self, idTipoCuenta: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM catalogo WHERE tipoCuenta = %s"
                cursor.execute(query, (idTipoCuenta,))
                rows = cursor.fetchall()
                return [Catalogo.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar las cuentas por tipo de cuenta: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
        
    def buscarPorCuentaPadre(self, cuentaPadre: int):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM catalogo WHERE cuentaPadre = %s"
                cursor.execute(query, (cuentaPadre,))
                rows = cursor.fetchall()
                return [Catalogo.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar las cuentas por cuenta padre: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []

    def buscarPorNombre(self, nombreCuenta: str):
        acceso = self.conexion.conectar()
        if acceso:
            try:
                cursor = acceso.cursor()
                query = "SELECT * FROM catalogo WHERE nombreCuenta LIKE %s"
                cursor.execute(query, (f"%{nombreCuenta}%",))
                rows = cursor.fetchall()
                return [Catalogo.from_row(row) for row in rows]
            except Exception as e:
                print(f"Error al listar las cuentas por nombre: {e}")
                return []
            finally:
                cursor.close()
        else:
            print("No se pudo establecer conexión a la base de datos.")
            return []
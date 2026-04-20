from BaseDeDatos.Conexion import Conexion
from Repositorios.TipoCuentaDAO import TipoCuentaDAO
from Entidades.TipoCuenta import TipoCuenta

class TipoCuentaService:

    def __init__(self):
        self.conexion_manager = Conexion()

    def crear_tipo_cuenta(self, data: TipoCuenta):
        """
        Gestiona la creación de un nuevo tipo de cuenta.
        Abre una conexión, realiza la operación y la cierra.
        """
        db_connection = None
        try:
            db_connection = self.conexion_manager.conectar()
            if db_connection:
                # El DAO ahora recibe la conexión activa
                tipo_cuenta_dao = TipoCuentaDAO(db_connection)
                tipo_cuenta_dao.insertar(data)
                db_connection.commit()
                print("Tipo de cuenta creado exitosamente y transacción confirmada.")
        except Exception as e:
            print(f"Error en el servicio al crear tipo de cuenta: {e}")
            if db_connection:
                db_connection.rollback()
                print("Transacción revertida.")
        finally:
            if db_connection:
                self.conexion_manager.desconectar()

    def obtener_tipo_cuenta_por_id(self, id_tipo_cuenta: int):
        """
        Obtiene un tipo de cuenta por su ID.
        """
        db_connection = None
        try:
            db_connection = self.conexion_manager.conectar()
            if db_connection:
                tipo_cuenta_dao = TipoCuentaDAO(db_connection)
                tipo_cuenta = tipo_cuenta_dao.buscarPorId(id_tipo_cuenta)
                return tipo_cuenta
        except Exception as e:
            print(f"Error en el servicio al obtener tipo de cuenta: {e}")
            return None
        finally:
            if db_connection:
                self.conexion_manager.desconectar()

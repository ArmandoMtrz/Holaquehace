from BaseDeDatos.Conexion import Conexion
from Repositorios.TipoCuentaDAO import TipoCuentaDAO
from Entidades.TipoCuenta import TipoCuenta

if __name__ == "__main__":
    conexion = Conexion()
    conexion.conectar()
    conexion.desconectar()
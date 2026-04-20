from Entidades.TipoCuenta import TipoCuenta
from Servicios.tipo_cuenta_service import TipoCuentaService

if __name__ == "__main__":
    print("--- Demostración del nuevo esquema de programación ---")

    # 1. Instanciamos el servicio, que es nuestro punto de entrada a la lógica de negocio.
    servicio_tipo_cuenta = TipoCuentaService()

    # 2. Creamos una entidad (un objeto) con los datos que queremos guardar.
    #    Usaremos un ID alto para no chocar con datos existentes.
    nuevo_tipo_cuenta = TipoCuenta(
        idTipoCuenta=99,
        tipoCuenta="CUENTA DE PRUEBA DESDE EL SERVICIO",
        categoria="Activo",
        subcategoria="Activo Corriente"
    )

    # 3. Usamos el servicio para crear el nuevo tipo de cuenta.
    #    El servicio se encargará de toda la gestión de la conexión y la transacción.
    print(f"\nIntentando crear: {nuevo_tipo_cuenta.tipoCuenta}")
    servicio_tipo_cuenta.crear_tipo_cuenta(nuevo_tipo_cuenta)

    # 4. Usamos el servicio para buscar el dato que acabamos de insertar.
    print(f"\nBuscando el tipo de cuenta con ID: {nuevo_tipo_cuenta.idTipoCuenta}")
    tipo_cuenta_encontrado = servicio_tipo_cuenta.obtener_tipo_cuenta_por_id(nuevo_tipo_cuenta.idTipoCuenta)

    # 5. Mostramos el resultado.
    if tipo_cuenta_encontrado:
        print("\n¡Éxito! Se encontró el siguiente dato en la base de datos:")
        print(tipo_cuenta_encontrado)
    else:
        print("\nFallo: No se pudo encontrar el dato insertado.")

    print("--- Fin de la demostración ---")

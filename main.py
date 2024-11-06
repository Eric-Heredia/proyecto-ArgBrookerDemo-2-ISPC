import sys
from conn_db import DatabaseConnection
from dao.usuario_dao import UsuarioDAO
from dao.transaccion_dao import TransaccionDAO
from dao.portafolio_dao import PortafolioDAO
from dao.cotizacion_dao import CotizacionDAO
from dao.accion_dao import AccionDAO
from model.usuario import Usuario
from model.transaccion import Transaccion
from datetime import datetime

# Inicializar DAOs
db_connection = DatabaseConnection()
usuario_dao = UsuarioDAO(db_connection)
transaccion_dao = TransaccionDAO(db_connection)
portafolio_dao = PortafolioDAO(db_connection)
cotizacion_dao = CotizacionDAO(db_connection)
accion_dao = AccionDAO(db_connection)

# Variables globales
usuario_actual = None

def registrar_usuario():
    print("\n=== Registro de Nuevo Usuario ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cuil = input("CUIL: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    
    # Crear nuevo usuario con saldo inicial
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, cuil=cuil, email=email, contraseña=contraseña, saldo=1000000)
    usuario_dao.crear_usuario(nuevo_usuario)
    print("Usuario registrado exitosamente con un saldo inicial de $1,000,000.")

def iniciar_sesion():
    global usuario_actual
    print("\n=== Inicio de Sesión ===")
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    
    if usuario_dao.autenticar(email, contraseña):
        usuario_actual = usuario_dao.obtener_usuario_por_email(email)
        print("Inicio de sesión exitoso. ¡Bienvenido/a!")
    else:
        print("Credenciales incorrectas. Inténtalo nuevamente.")

def mostrar_datos_cuenta():
    if not usuario_actual:
        print("Debes iniciar sesión primero.")
        return
    print("\n=== Datos de la Cuenta ===")
    print(f"Nombre: {usuario_actual.nombre} {usuario_actual.apellido}")
    print(f"Saldo: ${usuario_actual.saldo:.2f}")
    print(f"Total Invertido: ${calcular_total_invertido():.2f}")

def mostrar_portafolio():
    if not usuario_actual:
        print("Debes iniciar sesión primero.")
        return
    print("\n=== Mi Portafolio ===")
    portafolio = portafolio_dao.obtener_portafolio_por_usuario(usuario_actual.id)
    for accion in portafolio:
        print(f"Empresa: {accion['empresa']}, Cantidad: {accion['cantidad']}, Valor actual: ${accion['valor_actual']:.2f}")

def consultar_cotizaciones():
    print("\n=== Cotizaciones de Acciones ===")
    cotizaciones = cotizacion_dao.listar_cotizaciones()
    for cotizacion in cotizaciones:
        print(f"Símbolo: {cotizacion['simbolo']}, Empresa: {cotizacion['nombre']}")
        print(f"Último Operado: {cotizacion['ultimo_operado']}")
        print(f"Precio Compra: ${cotizacion['precio_compra']:.2f}, Precio Venta: ${cotizacion['precio_venta']:.2f}")
        print("-" * 30)

def comprar_accion():
    if not usuario_actual:
        print("Debes iniciar sesión primero.")
        return
    print("\n=== Comprar Acción ===")
    simbolo = input("Ingrese el símbolo de la acción que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    
    cotizacion = cotizacion_dao.obtener_cotizacion_por_simbolo(simbolo)
    if not cotizacion:
        print("Acción no encontrada.")
        return

    precio_compra = cotizacion['precio_compra']
    total = precio_compra * cantidad
    comision = total * 0.015
    total_con_comision = total + comision

    if usuario_actual.saldo < total_con_comision:
        print("Saldo insuficiente para esta operación.")
        return
    
    transaccion = Transaccion(usuario_id=usuario_actual.id, accion_id=cotizacion['accion_id'], cantidad=cantidad, tipo="compra", precio=precio_compra, fecha=datetime.now(), comision=comision)
    transaccion_dao.registrar_transaccion(transaccion)
    usuario_actual.saldo -= total_con_comision
    usuario_dao.actualizar_usuario(usuario_actual)
    print(f"Compra exitosa. Se aplicó una comisión de ${comision:.2f}.")

def vender_accion():
    if not usuario_actual:
        print("Debes iniciar sesión primero.")
        return
    print("\n=== Vender Acción ===")
    simbolo = input("Ingrese el símbolo de la acción que desea vender: ")
    cantidad = int(input("Ingrese la cantidad que desea vender: "))
    
    cotizacion = cotizacion_dao.obtener_cotizacion_por_simbolo(simbolo)
    if not cotizacion:
        print("Acción no encontrada.")
        return

    portafolio = portafolio_dao.obtener_portafolio_por_usuario(usuario_actual.id)
    accion_en_portafolio = next((accion for accion in portafolio if accion['simbolo'] == simbolo), None)
    
    if not accion_en_portafolio or accion_en_portafolio['cantidad'] < cantidad:
        print("Cantidad de acciones insuficiente en el portafolio.")
        return
    
    precio_venta = cotizacion['precio_venta']
    total = precio_venta * cantidad
    comision = total * 0.015
    total_con_comision = total - comision

    transaccion = Transaccion(usuario_id=usuario_actual.id, accion_id=cotizacion['accion_id'], cantidad=cantidad, tipo="venta", precio=precio_venta, fecha=datetime.now(), comision=comision)
    transaccion_dao.registrar_transaccion(transaccion)
    usuario_actual.saldo += total_con_comision
    usuario_dao.actualizar_usuario(usuario_actual)
    print(f"Venta exitosa. Se aplicó una comisión de ${comision:.2f}.")

def calcular_total_invertido():
    transacciones = transaccion_dao.obtener_transacciones_por_usuario(usuario_actual.id)
    total_invertido = sum(transaccion['precio'] * transaccion['cantidad'] for transaccion in transacciones if transaccion['tipo'] == "compra")
    return total_invertido

def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Mostrar datos de la cuenta")
        print("4. Mostrar portafolio")
        print("5. Consultar cotizaciones")
        print("6. Comprar acción")
        print("7. Vender acción")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            mostrar_datos_cuenta()
        elif opcion == "4":
            mostrar_portafolio()
        elif opcion == "5":
            consultar_cotizaciones()
        elif opcion == "6":
            comprar_accion()
        elif opcion == "7":
            vender_accion()
        elif opcion == "8":
            print("Gracias por usar la aplicación.")
            sys.exit()
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

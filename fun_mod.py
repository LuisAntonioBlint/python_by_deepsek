#EJERCICIO DE TRANSICIÓN:
from os import system
import datetime as dt     #importa la librería datetime para recursos de fechas y horas, incluyendo un alias para su comoda manipulación
import sys

#se define un inventario 
inventario_base = [
    {"nombre": "martillo", "precio": 25.50, "cantidad": 18},
    {"nombre": "desarmador", "precio": 45.20, "cantidad": 60},
    {"nombre": "clavo", "precio": 0.50, "cantidad": 585},
    {"nombre": "tornillo", "precio": 0.25, "cantidad": 2000}
]

# funcion para limpiar la terminal
def limpiar_pantalla():
    if system("clear") != 0: system("cls")

#funcion para mostrar el inventario actual
def mostrar_inventario(inventario):
    limpiar_pantalla()
    print('*'*63)
    print('Inventario actual\n'.center(63))
    for producto in inventario:
        print(f'|  {producto["nombre"]:15}  |  {producto["precio"]:7.2f}  |  {producto["cantidad"]:10}  |'.center(63))
    print('*'*63)
    opcion = int(input('\nIngresa 1 si deseas realizar algo más, si no pulsa 2 '))
    if opcion == 1:
        main()
    else:
        sys.exit()

#funcion para añadir un nuevo producto
def add_producto(inventario):
    limpiar_pantalla()
    nuevo_elemento = {"nombre": "", "precio": 0.00, "cantidad": 0}
    nuevo_elemento["nombre"] = input('Ingesa el nombre del producto: ')
    nuevo_elemento["precio"] = float(input('Ingesa el precio del producto: '))
    nuevo_elemento["cantidad"] = int(input('Ingesa la cantidad del producto: '))
    inventario.append(nuevo_elemento)

    opcion = int(input('\nIngresa 1 si deseas realizar algo más, si no pulsa 2 '))
    if opcion == 1:
        main()
    else:
        sys.exit()

#funcion para generar el reporte
def generar_reporte(inventario):
    limpiar_pantalla()
    total = 0.00 #inicializa el total en ceros
    fecha = dt.date.today().strftime("%d/%m/%Y") #establece la fecha al día de hoy
    
    print("*" * 63)
    print(f'[{fecha}] REPORTE DE INVENTARIO \n')
    for producto in inventario:
        total_por_producto = producto["precio"] * producto["cantidad"]
        print(f'|  {producto["nombre"]:15}  |  {producto["precio"]:7.2f}  |  {producto["cantidad"]:10}  |  {total_por_producto:10.2f}  |')    
        total += total_por_producto
    print(f'Valor total del inventario: {total:.2f}')
    print("*"*63)
    opcion = int(input('\nIngresa 1 si deseas realizar algo más, si no pulsa 2 '))
    if opcion == 1:
        main()
    else:
        sys.exit()
    
def mostrar_menu():
    limpiar_pantalla
    print('*'*63)
    print('Bienvenido al sistema de gestión de inventarios'.center(63))
    print('*'*63)
    print('1. Mostrar el inventario actual')
    print('2. Añadir un un nuevo producto')
    print('3. Generar un reporte completo')
    print('4. Salir')
    print('*'*63)


def main():
    limpiar_pantalla()
    mostrar_menu()
    opcion = input('¿Que harás hoy? ')
    match opcion:
        case '1':
            mostrar_inventario(inventario_base)
        case '2':
            add_producto(inventario_base)
        case '3':
            generar_reporte(inventario_base)
        case '4':
            sys.exit()


main()
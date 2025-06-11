#EJERCICIO DE TRANSICIÓN:
from os import system
import datetime as dt     #importa la librería datetime para recursos de fechas y horas, incluyendo un alias para su comoda manipulación


def limpiar_pantalla():
    if system("clear") != 0: system("cls")

#se define un inventario 
inventario_base = [
    {"nombre": "martillo", "precio": 25.50, "cantidad": 18},
    {"nombre": "desarmador", "precio": 45.20, "cantidad": 60},
    {"nombre": "clavo", "precio": 0.50, "cantidad": 585},
    {"nombre": "tornillo", "precio": 0.25, "cantidad": 2000}
]
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
    print(f'Valor total del inventario: {total}')
    print("*"*63)
    
# Llamada a la función
generar_reporte(inventario_base)
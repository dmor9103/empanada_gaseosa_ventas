import pandas as pd
from datetime import date
import time
import os
from os import system
from modules import tittle
from modules import read_csv
from modules import menus
from modules import cmd_control


def eliminar_producto(df, producto_a_eliminar):
    df = df[df['id'] != producto_a_eliminar]
    return df

def reorganizar_ids(df):
    df['id'] = range(1, len(df) + 1)
    return df

if __name__ == '__main__':
    tamaño_titulo = cmd_control.ventana()
    csv_archive = 'archivo.csv'
    contador_0 = 1
    while contador_0 == 1:
        contador = 1
        while contador == 1:    
            tittle.letrero('- Venta de Gaseosa -', tamaño_titulo)
            a = menus.main_menu()
            contador = menus.si_no(a, 4)

        contador = 1
        while contador == 1:
            if a == 1:
                # esto es para vender
                contador = 1
                while contador == 1:
                    tittle.letrero('- Vender -', tamaño_titulo)
                    df = read_csv.read_csv(csv_archive)
                    ultimo_id = df['id'].iloc[-1]

                    producto_modificar = menus.money_money(df.to_string(index=False))
                    if producto_modificar == 0:
                        print('saliste')
                        contador = 0
                    elif producto_modificar < (ultimo_id - ultimo_id) or producto_modificar > ultimo_id:
                        print('Opcion Invalida')
                        time.sleep(1)
                    else:
                        while True:
                            try:
                                ventas_a_sumar = int(menus.input_tiempo(3))
                                break
                            except ValueError:
                                ('')
                                print("Opcion Invalida")
                                time.sleep(0.5)

                        df.loc[df['id'] == producto_modificar, 'ventas'] += ventas_a_sumar
                        df.to_csv(csv_archive, index=False)
                        producto_modificar -= 1
                        print(f"Se han sumado {ventas_a_sumar} ventas a {df.iloc[producto_modificar, 1]}.")

            elif a == 2:
                # esto elimina un producto
                # esto llama a la función para reorganizar los IDs
                contador = 1
                while contador == 1:
                    tittle.letrero('- Agregar o Eliminar un producto -', tamaño_titulo)
                    df = read_csv.read_csv(csv_archive)
                    opcion = menus.agregar_eliminar(df.to_string(index=False))
                    
                    if opcion == 1:
                        # esto es para agregar un producto
                        df = read_csv.read_csv(csv_archive)
                        last_number = read_csv.column_csv(df, 'id')

                        nombre_producto = input('Cual es el producto: ')
                        precio_producto = int(input('Cual es el precio del producto: '))

                        nuevo_producto = {'id': last_number + 1, 'productos': nombre_producto,'precio': precio_producto, 'ventas': 0, 'total': 0}
                        nuevo_df = pd.DataFrame([nuevo_producto])
                        df = pd.concat([df, nuevo_df], ignore_index=True)
                        df.to_csv(csv_archive, index=False)
                        del nuevo_df
                        print('Se ha agregado el producto ', nombre_producto, ' al inventario')
                        time.sleep(3)
                    elif opcion == 2:
                        # Eliminar producto
                        df = read_csv.read_csv(csv_archive)

                        producto_a_eliminar = int(input("Ingrese el id del producto a eliminar: "))
                        nombre_producto_eliminado = df[df['id'] == producto_a_eliminar]['productos'].values[0]
                        df = eliminar_producto(df, producto_a_eliminar)
                        df = reorganizar_ids(df)
                        df.to_csv(csv_archive, index=False)
                        print('Se ha eliminado el producto ', producto_a_eliminar, ' del inventario')
                        time.sleep(1)
                    elif opcion == 0:
                        print('saliste')
                        time.sleep(1)
                        contador = 0
                    else:
                        print('Opcion invalida')
                        time.sleep(0.5)

            elif a == 3:
                # esto calcula el total de los productos vendidos
                df = read_csv.read_csv(csv_archive)
                tittle.letrero('- Calcular Total -', tamaño_titulo)

                df['total'] = df['precio'] * df['ventas']
                df.to_csv(csv_archive, index=False)
                total_ventas = df['total'].sum()
                print("El total es: ", total_ventas)
                time.sleep(1)

                reset = menus.make_reset()
                if reset == 1:
                    i = date.today()
                    ruta = 'C:/test/'
                    archivo_csv = str(ruta) + str(i) + " - " + str(csv_archive)
                    df.to_csv(archivo_csv, index=False)
                    time.sleep(0.5)
                    os.startfile(ruta)
                    print('')
                    print('Archivo creado en la ruta ', ruta)
                    time.sleep(3)

                    contador = 0
                elif reset == 2:
                    reset = menus.reset_comfirm()
                    if reset == 1:
                        print('')
                        df['ventas'] = 0
                        df['total'] = 0
                        df.to_csv(csv_archive, index=False)
                        time.sleep(1)
                        contador = 0
                    else:
                        contador = 0
                else:
                    print('Opcion invalida')
                    time.sleep(1)

            if a == 4:
                system('cls')
                menus.creado_por()
                break

            if a == 0:
                contador_0 = 0
                contador = 0
        
    system('cls')
    menus.salir()
    time.sleep(2)
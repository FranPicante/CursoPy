print('*** sistema de inventario funciones ***')

inventario=[
    {'id' : 1, 'nombre' : 'casa' , 'precio' : 30},
    {'id' : 2, 'nombre' : 'yo' , 'precio' : 30},
    {'id' : 3, 'nombre' : 'pantalo' , 'precio' : 30},
]

def mostrar_inventario():
    for producto in inventario:
        print(f'''--inventario--
                id = {producto.get('id')}
                nombre = {producto.get('nombre')}
                precio = {producto.get('precio')}
                ''')
        
def agregar_produto():
    pass

def buscar_id():
    pass

if __name__ == '__main__':
    while True:
        print('''--menu de opciones--
              1. mostrar productos
              2. agregar productos
              3. buscar por id
              4. salir''')
        
        opcion = int(input('elegir opcion: '))
        
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_produto()
        elif opcion == 3:
            buscar_id()
        elif opcion == 4:
            print('cerrando programa')
            break
        else:
            print('opcion invalida')
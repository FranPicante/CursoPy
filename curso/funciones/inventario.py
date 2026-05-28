print('*** sistema de inventario funciones ***')

inventario=[
    {'id' : 1, 'nombre' : 'casa' , 'precio' : 30},
    {'id' : 2, 'nombre' : 'yo' , 'precio' : 25},
    {'id' : 3, 'nombre' : 'pantalo' , 'precio' : 70},
]

def mostrar_inventario():
    print('--inventario--')
    for producto in inventario:
        print(f'''
                id = {producto.get('id')}
                nombre = {producto.get('nombre')}
                precio = {producto.get('precio')}
                ''')
        
def agregar_produto():
    numeroproc = int(input('ingrese el numero de productos para agregar: '))
    for indice in range(numeroproc):
        id = int(input('ingresar el id: '))
        nombre = input('ingresar el nombre: ')
        precio = float(input('ingresar el precio: '))

        producto = {'id' : id, 'nombre' : nombre, 'precio' : precio}

        inventario.append(producto)

def buscar_id():
    buscar = int(input('ingresar el id del producto que desea buscar: '))
    producto_encontrado = None

    for producto in inventario:
        if producto.get('id') == buscar:
            producto_encontrado = producto
            break
    if producto is not None:
            print(f'''---producto encontrado---
                id: {producto.get('id')}
                nombre: {producto.get('nombre')}
                precio: {producto.get('precio')}''')
    else:
        print('producto no encontrado')
    
    
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
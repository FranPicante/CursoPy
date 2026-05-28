print('*** maquina de snack ***\n')

snack = [
    {'id' : 1, 'nombre' : 'papas' , 'precio' : 23.50},
    {'id' : 2, 'nombre' : 'coca' , 'precio' : 15.00},
    {'id' : 3, 'nombre' : 'turron' , 'precio' : 20.00},
]

compras = []

def mostrar():
    print('***stock***')
    for producto in snack:
        print(f'''id: {producto.get('id')} {producto.get('nombre')} {producto.get('precio')}
--------''')

def comprar():
    compra = int(input('ingresa el id del producto: '))
    for producto in snack:
        if producto.get('id') == comprar:
    pass

def buscar_snack(compra):
    for producto in snack:
        if producto.get('id') == compra:
            
            break

def ticket():
    pass

if __name__ == '__main__':
     while True:
         print('*** Menu ***\n' \
         '1. Mostrar productos\n' \
         '2. comprar\n' \
         '3. mostrar ticket\n' \
         '4. salir\n')
         opcion = int(input('ingresar la opcion: '))

         if opcion == 1:
            mostrar()
         if opcion == 2:
             comprar()
         if opcion == 3:
             ticket()
         if opcion == 4:
             break
         else:
             print('opcion no valida')

    
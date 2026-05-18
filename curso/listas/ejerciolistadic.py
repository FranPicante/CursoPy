print('*** lista de procuctos ***')

inventario = []
numproduc = int(input('ingresa el numero de productos: '))

cont = 0

for indice in range(numproduc): #va a repetir hasta que el indice sea igual al numero
    print(f'ingresar datos del producto {indice + 1}: ')
    nombre = input('nombre del producto: ')
    valor =float(input('valor: '))
    stock = int(input('stock: '))
    
    producto = {'id':indice, 'nombre' : nombre, 'valor' : valor, 'stock' : stock}
    inventario.append(producto)

print(inventario)

#buscar un producto por el id

id_buscar = int(input('ingres el id del producto a buscar: '))

producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('informacion del producto')
    print(f'''id: {producto_encontrado.get('id')}
            nombre: {producto_encontrado.get('nombre')}
            valor: {producto_encontrado.get('valor')}
            stock: {producto_encontrado.get('stock')}''')
else:
    print('id no existe')

print('*** lista de productos ordenada ***')

for producto in inventario:
    print(f'''id: {producto.get('id')}
            nombre: {producto.get('nombre')}
            valor: {producto.get('valor')}
            stock: {producto.get('stock')}''')
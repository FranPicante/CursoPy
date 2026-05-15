print('*** lista de procuctos ***')

inventario = []
numproduc = int(input('ingresa el numero de productos'))

cont = 0

for indice in range(numproduc): #va a repetir hasta que el indice sea igual al numero
    print(f'ingresar el valor del producto {indice + 1}')
    nombre = input('nombre del producto: ')
    valor =float(input('valor: '))
    stock = int(input('stock: '))
    
    producto = {'id':indice, 'nombre' : nombre, 'valor' : valor, 'stock' : stock}

print(inventario)


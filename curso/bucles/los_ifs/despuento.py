n_productos = 10
cantidad = int(input('ingresar cantidad de productos comprados: '))
miembro = input('es miembro (Si/No): ')

aplica = (n_productos >= cantidad and miembro.strip().lower()=='si')

print (f'se puede aplicar descuento: {aplica}')
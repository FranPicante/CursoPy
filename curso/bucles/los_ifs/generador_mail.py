#pedir datos
nombre = input('ingresar nombre: ')
apellido = input('ingresar apellido: ')
empresa = input('ingrasar nombre de la empresa: ')

#normalizar datos
#strip quita los espacios al princio y al final. lower hace que sea todo minusculas. replace intercambia el primer ' ' por el segundo ' '
nombre = nombre.strip().lower().replace(' ','.')
apellido = apellido.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','') #aqui se cambian los espacios por una cadena vacia

email = f'{nombre}{apellido}@{empresa}.com'

print(f'{email}')

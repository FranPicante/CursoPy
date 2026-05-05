user = 'admin'
password = 'yo123'

ingresar_user = input('ingrese el numbre de usuario: ')
ingresar_password = input('ingrese la clave: ')

comprobar =  (user == ingresar_user.strip() and password == ingresar_password.strip())

print (f'las credenciales son correctas: {comprobar}')
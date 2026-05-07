usuario = 'yo'
clave = '123'
user = input('igrese el usuario: ')
password = input('digite la clave: ')

user = user.strip()
password = password.strip()

if user == usuario and password == clave:
    print('de 10 entra')
elif usuario == user:
    print('clave erronea')
elif password == clave:
    print('usuario erroneo')
else:
    print('todo mal')
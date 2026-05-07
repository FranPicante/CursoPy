edad =int(input('ingresa tu edad: '))
miedo = input('tenes miedo a la oscuridad: ')

miedo = miedo.strip().lower() == 'si'

if not miedo and edad >= 10:
    print('podes entrar')

else:
    print('sos cagon, no entras')

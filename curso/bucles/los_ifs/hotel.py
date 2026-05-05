sin_vista = 150.50
con_vista = 190.50

dias = int(input('cuantos dias?: '))
vista = input('quiere vista al mar: ')
vista = vista.strip().lower() == 'si' #si es si entonces es true si no false

quiere = 'si' if vista else 'no'

if vista:
    precio = con_vista * dias
    print(f'el precio es de {precio}'
          f'\n ')
else:
    precio = sin_vista * dias
    print(f'el precio es de: {precio}')
     
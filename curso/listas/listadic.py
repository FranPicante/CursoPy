
lista = [
    '0' : {
        'nombre' : 'yo'
        'apellido' : '123'
        'fecha nacimiento' : 0
    },
    
    '1' : {
        'nombre' : 'oy'
        'apellido' : '321'
        'fecha nacimiento' : 1
    }
]

print(f'nombre: {lista[0].get('nombre')}')
print(f'apellido: {lista[0].get('apellido')}')
print(f'fecha de nac: {lista[0].get('fecha nacimiento')}')
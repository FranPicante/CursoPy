
print('agenda de contactos')

agenta = {
    'carlos' : {
        'telefono' : '3811',
        'email' : 'carlos',
        'direcion' : 'calle123'
    },
    'maria' : {
        'telefono' : '3812',
        'email' : 'maria@',
        'direcion' : 'calle456'
    },
    'pedro' : {
        'telefono' : '3813',
        'email' : 'pedro@',
        'direcion' : 'calle789'
    }
}

print(agenta)

for nombres, detalles in agenta.items(): #nombre son los nombres de las personas de las lista
    #detalles son los datos dentro de las personas
    print(f'''nombre: {nombres}
    telefono: {detalles.get('telefono')}
    mail: {detalles.get('email')}
    direccion: {detalles.get('direcion')}''')

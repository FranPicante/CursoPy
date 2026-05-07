minimo = 1000
monto = float(input('ingresar el monto de la compra: '))
miembro = input('es miembro: ')

miembro = miembro.strip().lower()

if monto == minimo and miembro == 'si':
    descuento = 0.10
    monto_descuento = monto-(monto * descuento)
    print(f'tiene descuento del: {descuento*100}%\n' \
          f'precio de la compra: {monto}\n'\
            f'precio con descuento: {monto_descuento} ')


elif monto <= minimo and miembro == 'si':
    descuento = 0.05
    monto_descuento = monto-(monto * descuento)
    print(f'tiene un descuento del {descuento*100}%:\n' \
          f'precio de la compra: {monto}\n'\
            f'precio con descuento: {monto_descuento} ')

else:
    print('no tiene descuento\n'\
    f'su compra es de: {monto}')
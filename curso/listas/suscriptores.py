suscriptores = set()
numsus = int(input('ingrese el numero de suscriptores: '))

#print('opciones:' \
#'1 crear una lista' \
#'2 agregar un suscritor nuevo' \
#'3 eliminar un suscriptor' \
#'0 salir')
#opcion = int(input('elegir opcion: '))


for _ in range(numsus): # el _ es porque no tiene indice y range es hasta que sea el numsus
    suscriptores.add(input('ingresa el mail de suscriptor: '))

print(f'lista inicial: {suscriptores}')

nuevosub = input('ingresar el nuevo sub: ')
if nuevosub in suscriptores:
    print('el sub ya estaba en la lista')
else:
    print('nuevo sub gregado')
    suscriptores.add(nuevosub)
    print(f'la nueva lista es: {suscriptores}')

eliminarsub = input('ingrese el que va a eliminar: ')
if eliminarsub in suscriptores:
    suscriptores.remove(eliminarsub)
    print(f'sub eliminado\n nueva lista {suscriptores}')
else:
    print(f'sub no se encuentra en lista {suscriptores}')
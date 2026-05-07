
total_notas = int(input('ingresar la cantidad de notas: '))
notas = []

for indice in range (total_notas):
    nota = float(input(f'ingresa la nota {indice+1}: '))
    notas.append(nota)

print(f'\ntodas las notas son {notas}')

promedio = sum(notas) / total_notas

print(f'\n el promedio es: {promedio}')
from random import randint

print('***JUEGUITO***\n')

numrandom = randint (1 ,50)
intentos = 0
intentos_max = 10

numero = int(input('ingresa un numero entre 1 y 50: ')) 

while  numrandom != numero and intentos <= intentos_max:
    print(f'intendo numero: {intentos}\n')

    if numero < numrandom:
        print('el numero es mayor, volve a intentar\n')
        numero = int(input('intenta de nuevo: '))
    
    elif numero > numrandom:
        print('el numero es menor, volve a intentar\n ')
        numero = int(input('intenta de nuevo: '))
    
    intentos += 1

if numero == numrandom:
    print(f'ganaste en {intentos}')
else:
    print(f'perdiste el numero era: {numrandom}')

print('*** potencia de un numero ***')

numero =int(input('ingresa un numero'))
potencia = int(input('ingresa una potencia'))

def calculo_potencia (numero,potencia):
    if potencia == 0:
        print(f'{numero} elevado a {potencia} es igual a 1')
    else:
        calculo_parcial = numero * calculo_potencia(numero,potencia - 1)
    return calculo_parcial

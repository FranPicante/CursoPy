print('*** factorial de un numero ***')

def factorial (numero):
    if numero == 0 or numero == 1:
        print(f'el factorial de {numero} es 1')
        return 1
    else:
        factorial_parcial = numero * factorial(numero - 1)
        print(f'el resultado del factorial parcial de {numero} es {factorial_parcial}')
        return factorial_parcial

numero = 5
resultado = factorial(numero)

print(f'el factorial de {numero} es {resultado}')

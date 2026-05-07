saldo1 = 1000
salir = False 

while not salir:
    print('''**OPCIONES**
          1. CONSULTAR SALDO
          2. RETIRAR
          3. DEPOSITAR
          4. SALIR''')
    opcion = int(input('seleccione la opcion: '))
    
    if opcion == 1:
        print(f'tu saldo es de: {saldo1}\n')

    elif opcion == 2:
        retiro = float(input('cuanto queres retirar: '))
        if retiro <= saldo1:
            saldo1 -= retiro
            print(f'tu nuevo saldo es: ${saldo1}\n')
        else:
            print('saldo insuficiente, volver a intentar\n')

    elif opcion == 3:
        ingreso = float(input('ingresa el monto a depositar: '))
        saldo1 += ingreso
        print(f'saldo actual: ${saldo1}\n')

    elif opcion == 4:
        salir = True
        print('chau\n')
    
    else:
        print('opcion no valida')
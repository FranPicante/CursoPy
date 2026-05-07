primero = int(input('ingresa un numero: '))
segundo = int(input('ingresa otro: '))

if primero == segundo:
    print('los numeros son iguales')
    
elif primero < segundo:
    print(f'{segundo} es mayor que {primero}')
    
else:
    print(f'{primero} es mayo que {segundo}')
nota = int(input('ingresar la nota: '))

if nota > 9 and nota <= 10:
    print('tenes una A')
    
elif nota >= 8 and nota < 9:
    print('tenes una B')

elif nota >=7 and nota < 8:
    print('tenes una C')

elif nota >=6 and nota < 7:
    print('tenes una D')

elif nota >= 0 and nota < 6:
    print('tenes una F')

else:
    print('valor desconocido')
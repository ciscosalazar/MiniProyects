#Ejercicio de programacion - Calculadora simple

try: 
    primero = int(input('Ingrese primer número: '))
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

try:
    segundo = int(input('Ingrese segundo número: '))
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('Divison:', primero / segundo)
else:
    print('El simbolo ingresado no es valido')
    

# Algoritmo del morral se conoce como "Algoritmo Codicioso"
def morral(tamano_morral, masas, valores, n):
    print(tamano_morral, masas, valores, n)
    # PRIMER CASO BASE
    # Si la longitud de la lista es 0, o el tamaño del morral el 
    # 0 devuelvo el numero 0.

    if n == 0 or tamano_morral == 0:
        print('opc 1')
        return 0

    # SEGUNDO CASO BASE
    # Si la masa es mayor de la que 
    # puedo guardar, entonces, sigo con el siguiente elemento de la lista.
    if masas[n - 1] > tamano_morral:
        print('opc 2')
        return morral(tamano_morral, masas, valores, n - 1)

    print('opc 3')
    return max(valores[n - 1] + morral(tamano_morral - masas[n - 1], masas, valores, n - 1), 
                morral(tamano_morral, masas, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120] # Valores en dolares
    masas = [10, 20, 30]
    tamano_morral = 30  # Tamaño del morral, cuantos kg de masa puede cargar
    n = len(valores)

    resultado = morral(tamano_morral, masas, valores, n)
    
    # retorna el valor maximo que podemos tener en nuestro morral segun su tamaño
    print(f'puedo cargar {resultado} dolares en metales preciosos')
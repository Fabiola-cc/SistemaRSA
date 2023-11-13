'''
Universidad del Valle de Guatemala
Proyecto Final - Matemática Discreta
Sistema de encriptación RSA
 ---> Cálculos

Fabiola Contreras 22787
María José Villafuerte 22129
'''

def encriptado(M, P, Q, E):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    diccionario_letras = {letra: indice for indice, letra in enumerate(alfabeto)}

    return 0

def desencriptado(C, E, N):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    diccionario_letras = {letra: indice for indice, letra in enumerate(alfabeto)}

    primos = factorizacion_prima(N)
    fi = (primos[0] -1)*(primos[1] -1)
    mensaje = ""

    #Encontrar llave privada 'd' --> Ed - fiY = 1
    solucion = resolver_ecuacion(E, fi, 1)
    d = solucion[0] % fi
    
    #Encontrar las letras decodificadas
    bloques = [C[i:i+4] for i in range(0, len(C), 4)]
    decode = ""
    for bloque in bloques:
        decode += str(mod_exponent(int(bloque), d, N))

    letras = [decode[i:i+2] for i in range(0, len(decode), 2)]
    for val in letras:
        for letra, valor in diccionario_letras.items():
            if valor == int(val):
                mensaje += letra
                break
    
    return mensaje, d

def factorizacion_prima(numero):
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if (numero % divisor) == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return factores_primos

def euclides_extendido(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclides_extendido(b, a % b)
        return d, y, x - (a // b) * y

def resolver_ecuacion(a, b, c):
    d, x, y = euclides_extendido(a, b)

    if c % d == 0:
        x0 = x * (c // d)
        y0 = y * (c // d)
        return x0, y0
    else:
        return None

def mod_exponent(num, exp, mod):
    if exp == 0:
        return 1
    if exp%2 == 0:
        result = mod_exponent(num, exp // 2, mod)
        return (result * result) % mod
    else:
        return (num * mod_exponent(num, (exp-1), mod)) % mod
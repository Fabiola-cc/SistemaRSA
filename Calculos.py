'''
Universidad del Valle de Guatemala
Proyecto Final - Matemática Discreta
Sistema de encriptación RSA
 ---> Cálculos

Fabiola Contreras 22787
María José Villafuerte 22129
'''
def encriptado(mensaje, P, Q, elemento_llave_E):
    #Limpa el mensaje para que no tenga espacios ni mayusculas
    mensaje = ''.join(mensaje.split())
    mensaje = mensaje.lower()

    #Realizar el diccionario
    alfabeto = 'klmnopqrstuvwxyz'
    diccionario_letras_finales = {letra: indice+10 for indice, letra in enumerate(alfabeto)}
    alfabeto = 'abcdefghij'
    diccionario_letras = {letra: str(indice).zfill(2) for indice, letra in enumerate(alfabeto)}
    diccionario_letras.update(diccionario_letras_finales)

    #Crear los elementos d ela llace, al igual que los elementos que nos sirven para encriptar
    elemento_llave_n = P*Q
    phi = (P - 1) * (Q - 1)

    mensaje_encriptado = ""

    #Si el módulo entre el e y phi no es uno, no podemos realizar el trabajo 
    if calcular_mcd(elemento_llave_E,phi)==1:

        #Separamos el mensaje entre grupos de 2
        bloques = [mensaje[i:i+2] for i in range(0, len(mensaje), 2)]
        
        #Por cada grupo de dos vamos a hacer la encriptación
        for bloque in bloques:
            primera_letra = bloque[0]
            try:
                segunda_letra = bloque[1]
            except:
                #En caso de que no exista segunda letra se va a agregar h como cracter falso
                segunda_letra = 'h'
            indice_de_string = diccionario_letras[str(primera_letra)]
            indice_de_string_1 = diccionario_letras[str(segunda_letra)]
            letras_cifradas_sin_llave = str(indice_de_string) + str(indice_de_string_1)
            letras_cifradas_con_llave =  pow(int(letras_cifradas_sin_llave),elemento_llave_E)%elemento_llave_n

            #Para que la encriptación sea de como 0483 y no de forma erronea como 483 
            if len(str(letras_cifradas_con_llave)) < 4:
                letras_cifradas_con_llave = '{:04d}'.format(letras_cifradas_con_llave)
            mensaje_encriptado += str(letras_cifradas_con_llave) +" "
            #mensaje_encriptado += letras_cifradas_sin_llave
            
    else:
        mensaje_encriptado = "ERROR e debe de ser distinto"
    return mensaje_encriptado

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def desencriptado(C, E, N):
    C = ''.join(C.split())
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
    for bloque in bloques: #Decodificar numericamente por bloques de 4 dígitos
        Block_code = str(mod_exponent(int(bloque), d, N))
        if len(Block_code) == 3:
            Block_code = "0" + Block_code
        decode += Block_code

    letras = [decode[i:i+2] for i in range(0, len(decode), 2)] #Dividir letras como segmentos de 2 dígitos
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
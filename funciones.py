def decimal_a_binario(num):
    decimal = int(num)              # Convertimos el string en integer              
    binario = ''                    # Creamos el string vacio que ira sumando todos los residuos de dividir el decimal por 2.
    while decimal > 0:              
        binario = str(decimal % 2) + binario # Calculamos el residuo de dividir el decimal por 2 y lo sumamos a la variable binario
        decimal //= 2               # A la variable decimal, la volvemos a dividir por 2 y le asignamos el valor del cociente (sin la parte decimal) de la division
    if binario == '':               # Si el decimal es 0,
        binario = "0"               # el binario es 0
    return binario

def binario_a_decimal(num):         
    decimal = 0                     # Decimal sera la variable encargada de ir acumulando el resultado de multiplicar cada digito binario == 1 por su potencia de 2 
    potencia = 0                    # Potencia sera la variable encargada de ir incrementando la potencia de acuerdo al digito binario evaluado  
    for i in invertir_binario(num): # Como ya invertimos el binario, podemos recorrelo normalmente con un simple for
        if i == '1':                # Nos interesan solo las multiplicaciones donde el digito binario es == 1                          
            decimal += 2 ** potencia
        potencia += 1
    return decimal

def validar_decimal(num):
    try:
        return int(num)             # Si se puede convertir a entero, es decimal 'entero'
    except ValueError:              # Entrada no valida
        return None                 

def validar_binario(num):           # Esta funcion valida si la expresion recibida es una expresion binaria o no.
    for i in num:                   # Para ello evalua cada caracter de la cadena recibida verificando si los elementos son '0' o '1'
        if i not in ('0', '1'):     # Si no lo son, 
            return False            # retorna False
    return True                     # Si lo son, retorna True 

def invertir_binario(num):          # Esta funcion invierte la cadena recibida 
    binarioInvertido = ''           # Creamos la variable que recibira la cadena invertida
    for i in range(len(num)-1, -1, -1): # len(num)-1 nos da el indice del ultimo caracter de la cadena. Recorremos el binario de derecha a izquierda (-1)
        binarioInvertido += num[i]  # Sumamos cada caracter a la nueva cadena invertida. Como recorremos de derecha a izquierda, el ultimo caracter se convierte en el primero.
    return binarioInvertido

def menu():
    print("||===>>> ConverTron <<<===||")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")
    while True:
        opcion = input("Seleccione una opcion (1-3): ")
        if opcion == "1":           # Decimal a Binario
            numDec = input("Ingrese un numero decimal entero: ")
            num = validar_decimal(numDec)
            if num is None:
                print("ERROR. Por favor ingrese un numero decimal valido.")
            else:
                print(f"El numero {numDec} en binario es: {decimal_a_binario(num)}")
        
        elif opcion == "2":         # Binario a Decimal
            numBin = input("Ingrese un numero binario: ")
            if not validar_binario(numBin):
                print("ERROR: Debe ingresar un numero binario valido.")
            else:
                print(f"El numero binario {numBin} en decimal es: {binario_a_decimal(numBin)}")
        
        elif opcion == "3":         # Salir
            print("Hasta la vista Baby!")
            break
        else:
            print("ERROR. Por favor ingrese una opcion valida (1-3)")

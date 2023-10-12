def decimal_a_binario(decimal):
    return bin(decimal)

def decimal_a_hexadecimal(decimal):
    return hex(decimal)

def binario_a_decimal(binario):
    return int(binario, 2)

def binario_a_hexadecimal(binario):
    decimal = binario_a_decimal(binario)
    return decimal_a_hexadecimal(decimal)

def hexadecimal_a_binario(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal_a_binario(decimal)

def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

def es_binario_valido(binario):
    return all(bit == '0' or bit == '1' for bit in binario)

def es_hexadecimal_valido(hexadecimal):
    return all(char.isdigit() or char in 'ABCDEFabcdef' for char in hexadecimal)

while True:
    print("Elige una opción:")
    print("1. Decimal a Binario")
    print("2. Decimal a Hexadecimal")
    print("3. Binario a Decimal")
    print("4. Binario a Hexadecimal")
    print("5. Hexadecimal a Binario")
    print("6. Hexadecimal a Decimal")
    print("7. Salir")
   
    opcion = int(input("Opción: "))
   
    if opcion == 1:
        decimal = int(input("Ingresa un número decimal: "))
        resultado = decimal_a_binario(decimal)
        print("El número en binario es:", resultado)
    elif opcion == 2:
        decimal = int(input("Ingresa un número decimal: "))
        resultado = decimal_a_hexadecimal(decimal)
        print("El número en hexadecimal es:", resultado)
    elif opcion == 3:
        binario = input("Ingresa un número binario: ")
        if es_binario_valido(binario):
            resultado = binario_a_decimal(binario)
            print("El número en decimal es:", resultado)
        else:
            print("Entrada no válida. Ingresa un número binario válido.")
    elif opcion == 4:
        binario = input("Ingresa un número binario: ")
        if es_binario_valido(binario):
            resultado = binario_a_hexadecimal(binario)
            print("El número en hexadecimal es:", resultado)
        else:
            print("Entrada no válida. Ingresa un número binario válido.")
    elif opcion == 5:
        hexadecimal = input("Ingresa un número hexadecimal: ")
        if es_hexadecimal_valido(hexadecimal):
            resultado = hexadecimal_a_binario(hexadecimal)
            print("El número en binario es:", resultado)
        else:
            print("Entrada no válida. Ingresa un número hexadecimal válido.")
    elif opcion == 6:
        hexadecimal = input("Ingresa un número hexadecimal: ")
        if es_hexadecimal_valido(hexadecimal):
            resultado = hexadecimal_a_decimal(hexadecimal)
            print("El número en decimal es:", resultado)
        else:
            print("Entrada no válida. Ingresa un número hexadecimal válido.")
    elif opcion == 7:
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 7.")

print("Ejemplo doble condicional con Y (AND) o (OR)")
numero1 = input("ingresar numero 1: ")
numero2 = input("ingresar numero 2: ")

if (numero1 == '0' and numero2 == '0'):
    print("Se escribieron numero 1 y numero 2 con cero")
else: 
    print("numero 1 y numero 2 no contienen cero")

if (numero1 == '0' or numero2 == '0'):
    print("Se escribieron numero 1 o numero 2 con cero")
else: 
    print("numero 1 o numero 2 no contienen cero")


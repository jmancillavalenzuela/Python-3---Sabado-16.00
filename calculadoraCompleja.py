#Calculadora Simple (Suma y Resta)
print("Calculadora Compleja: ")

#numero1 corresponde al valor nunumeico de la variable dianmica
numero1 = input("Ingrese el valor del primer numero: ")

#numero2 corresponde al valor numerico de la variable dianmica
numero2 = input("Ingrese el valor del segundo numero: ")

#Mensaje por pantalla!
print("Que operacion desea ejecutar?")

operacion = ""
while(operacion is ""):
    print("Usted Ingreso: " + numero1 + " y " + numero2)
    #operacion corresponde al valor del simbolo de la variable dianmica
    operacion = input("Ingrese el simbolo de la operacion (+ , - , * , /): ")
    #Logica de la operacion:
    if operacion == '+':
        resultado = int(numero1) + int(numero2)
    else:
        if operacion == '-' :
            resultado = int(numero1) - int(numero2)
        else:
            if operacion == '*':
                resultado = int(numero1) * int(numero2)
            else:
                if operacion == '/' and numero2 is not '0': #==: IGUAL !=: NOT  is not: NOT
                    resultado  = int(numero1) / int(numero2)
                else:
                    print("ERROR: No Ingreso una operacion VALIDA") 
                    operacion = ""
print("Usted ingreso la operacion: " + operacion + " y su resultado es: " + str(resultado))
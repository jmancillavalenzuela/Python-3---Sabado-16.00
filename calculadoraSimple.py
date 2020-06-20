#Calculadora Simple (Suma y Resta)
print("Calculadora Simple: ")

#numero1 corresponde al valor numerico de la variable dianmica
numero1 = input("Ingrese el valor del primer numero: ")

#numero2 corresponde al valor numerico de la variable dianmica
numero2 = input("Ingrese el valor del segundo numero: ")

#Variable resultadoSuma contiene la sumatoria de numero1, numero2
resultadoSuma = int(numero1) + int(numero2)

#Variable resultadoResta contiene la resta de numero1, numero2
resultadoResta = int(numero1) - int(numero2)
resultadoResta2 = int(numero2) - int(numero1) 

#Variable resultadoMultiplicacion contiene la multiplicacion de numero1, numero2
resultadoMultiplicacion = int(numero1) * int(numero2)

#Para la division, el cero no puede ser contenido en numero2
#Pregunta si numero2 es igual a 0
if numero2 == '0': # "0" o '0' son validos, pero '0' es mas correcto
    print("No se puede Dividir por cero")  #Si el numero2 es cero, no se puede dividir
else: #De lo contrario (numero2 es distinto a 0)    
    if numero2 == '1':
        resultadoDivision = numero1
        print("La division del " + str(numero1) + " dividido por el " + str(numero2) + " es igual a: " + str(resultadoDivision))
    else:    
        resultadoDivision = int(numero1) / int(numero2) #Dividir numero 1 por numero2
        print("La division del " + str(numero1) + " dividido por el " + str(numero2) + " es igual a: " + str(resultadoDivision))

print("La suma del " + str(numero1) + " mas el " + str(numero2) + " es igual a: " + str(resultadoSuma))
print("La resta del " + str(numero1) + " menos el " + str(numero2) + " es igual a: " + str(resultadoResta))
print("La resta del " + str(numero2) + " menos el " + str(numero1) + " es igual a: " + str(resultadoResta2))
print("La multiplicacion del " + str(numero1) + " por el " + str(numero2) + " es igual a: " + str(resultadoMultiplicacion))

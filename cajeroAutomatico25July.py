#Cajero Automatico V2.0 / Pagar Cuentas

#Variables Iniciales 
ctaCte = 20
ahorro = 50
linea = 100
lineaInicial = linea

print("Qué operación quiere hacer: ") 
print ("1. Depositar fondos Cuenta Corriente.") #Solo efectivo
print ("2. Retirar fondos Cuenta Corriente.") # Retirar fondos 
print ("3. Depositar fondos Cuenta Ahorro.") #Extraer dinero de la Cta Cte y depositar a cta Ahorra
print ("4. Retirar fondos Cuenta Ahorro") #Depostiar dinero de la Cta Cte y extraer a cta Ahorra
print ("5. Salir del Programa.")

# LINEA DE SOBREGIRO SE ACTIVA CUANDO:
# Pago de una cuenta, o retiro de dinero; y no tengo el saldo suficiente en mi ctacte, por lo tanto pido prestado a mi linea de sobregiro (Pregunta si quiere pagar, SI o NO) ------
# Si la respuesta es NO; cancelar el retiro anterior (SALDO INSUFICIENTE) -----
# PAGO DE LA LINEA DE SOBREGIRO, CUANDO tenga el suficiente saldo en mi ctacte, y ademas yo acepto pagarla (Pregunta si quiere pagar, SI o NO) ----

#PROXIMA CLASE
# DESPUES de preguntar por 3era vez, si quiere pagar y la respuesta es NO; INFORMAR al usuario, un BLOQUEO DE CUENTA; Todas las funcionalidades bloquedas, hasta pagar.
# Retirar fondos en cuenta de ahorro; Depositar fondos en ctacte, Se alcanza el monto de deuda; pago de inmediato.
# Liberar Cuenta

decision = input("Seleccionar Opcion: ")

#Delacaracion de Variables para usuario *Manipulacion*
abono = ""
depAhorro = ""
retAhorro = ""
pagar = ""
contarNoPagoSobregiro = 0
salir = False #Variable para salir del programa #BOOLEAN VERDADERO O FALSO

while salir == False:
    if decision == '0':
        #Desplegar MENU
        print("-------------MENU----------------") 
        print("Qué operación quiere hacer: ") 
        print ("1. Depositar fondos Cuenta Corriente.") #Solo efectivo
        print ("2. Retirar fondos Cuenta Corriente.") # Retirar fondos 
        print ("3. Depositar fondos Cuenta Ahorro.") #Extraer dinero de la Cta Cte y depositar a cta Ahorra
        print ("4. Retirar fondos Cuenta Ahorro") ##Depostiar dinero de la Cta Cte y extraer a cta Ahorra
        print ("5. Salir del Programa.")
        decision = input("Seleccionar Opcion: ")
    else:   
        if decision == '1':
            print("Ud. va a realizar una operación de depósito")
            print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
            abono = int(input("Cuanto desea abonar: "))
            if lineaInicial > linea:
                debe = int(lineaInicial) - int(linea)
                print("Usted presenta una deuda en su linea de sobregiro")
                print("Se deben: ", debe, "a su linea de sobregiro")
                if contarNoPagoSobregiro > 3:
                    respuesta = "si"
                else:
                    respuesta = input("Desea pagar esta deuda? [SI] [NO] ")
                if respuesta == "SI" or respuesta == "Si" or respuesta == "si":
                        #Pagar el monto de mi linea de sobregiro
                        if abono >= debe:
                            linea = lineaInicial
                            auxiliar = int(abono) - int(debe) #Saldo faltante para cumplir la operacion
                            ctaCte = int(ctaCte) + int(auxiliar) #Cargo el dinero faltante a mi cta Cte
                            print("usted ha pagado su deuda con exito")
                            print("Su nuevo saldo en la linea de sobregiro es: ", linea)
                            print("Su nuevo saldo en la cuenta corriente es: ", str(ctaCte)) #Deberia dar un monto igual a 0
                            decision = "0"
                else:
                    if respuesta == "NO" or respuesta == "No" or respuesta =="no":
                        #Rechazar la operacion
                        contarNoPagoSobregiro += 1
                        ctaCte = int(ctaCte) + int(abono) #Cargo dinero a mi cta Cte
                        print("Su nuevo saldo en la cuenta corriente es: ", str(ctaCte))
                        decision = "0" #Volver al menu principal
        else: 
            if decision == '2':
                print("Ud. ha seleccionado pagar una deuda")
                print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
                pagar = int(input("Cuanto desea pagar: "))
                if pagar > ctaCte:
                    print("Su saldo actual es insuficente para realizar la operacion: " )
                    print("usted posee: :", ctaCte, "en su cuenta corriente" ) #Se puede concatenar una variable con texto con la COMA (,) al igual que el simbolo (+)
                    print("Usted quiere retirar: ", pagar)
                    print("Puede utilizar su linea de sobregiro para realizar esta operacion: ")
                    print("Usted posee una linea de sobregiro con un monto de: ", linea)
                    respuesta =  input("Desea utilizar su linea de sobregiro? [SI] [NO]: ")
                    if respuesta == "SI" or respuesta == "Si" or respuesta == "si":
                        #Pagar el monto restante con mi linea de sobregiro
                        auxiliar = int(pagar) - int(ctaCte) #Saldo faltante para cumplir la operacion
                        linea = int(linea) - int(auxiliar) #Le resto a mi linea de sobregiro, el monto faltante para realizar la operacion
                        ctaCte = int(ctaCte) + int(auxiliar) #Cargo el dinero faltante a mi cta Cte
                        ctaCte = int(ctaCte) - int(pagar) #Realizar el pago sin problemas
                        print("usted ha pagado su deuda con exito")
                        print("Su nuevo saldo en la linea de sobregiro es: ", linea)
                        print("Su nuevo saldo en la cuenta corriente es: ", str(ctaCte)) #Deberia dar un monto igual a 0
                        decision = "0"
                    else:
                        if respuesta == "NO" or respuesta == "No" or respuesta =="no":
                            #Rechazar la operacion
                            print("No se ha podido realizar la operacion, Usted no posee saldo suficiente")
                            decision = "0" #Volver al menu principal
                else:
                    #Se puede pagar sin problemas, pues saldo suficiente en ctaCte (pagar es menor que ctaCte)
                    ctaCte = int(ctaCte) - int(pagar)
                    print("usted ha pagado su deuda con exito")
                    print("Usted retiro: ", pagar)
                    print("Su nuevo saldo en la cuenta corriente es: ", str(ctaCte))
                    decision = "0"
            else:
                if decision == '3':
                    print("Ud. ha seleccionado deposito en cta ahorro")
                    print("Saldo cuenta corriente: " + str(ctaCte))
                    print("Saldo cuenta ahorro: " + str(ahorro))
                    
                    depAhorro = input("Cuanto desea depositar en su cta ahorro: ")
                    ahorro = int(ahorro) + int(depAhorro)
                    ctaCte = int(ctaCte) - int(depAhorro)         
                    print("Ud ha depositado con exito")
                    print("Su nuevo saldo en la cuenta corriente es: " + str(ctaCte))
                    print("Su nuevo saldo en la cuenta ahorro es: " + str(ahorro))
                    decision = "0"
                else:
                    if decision == '4':
                        print("Ud. ha seleccionado Retiro de fondos en cta ahorro")
                        print("Saldo cuenta corriente: " + str(ctaCte))
                        print("Saldo cuenta ahorro: " + str(ahorro))
                        
                        retAhorro = input("Cuanto desea retirar en su cta ahorro: ")
                        while int(retAhorro) > int(ahorro):
                        #if int(retAhorro) > int(ahorro): #WHILE
                            print("ERROR usted no tiene esa cantidad de fondos")
                            print("Saldo cuenta corriente: " + str(ctaCte))
                            print("Saldo cuenta ahorro: " + str(ahorro))
                            retAhorro = input("Cuanto desea retirar en su cta ahorro: ")
                        #else:    
                        ahorro = int(ahorro) - int(retAhorro)
                        ctaCte = int(ctaCte) + int(retAhorro)         
                        print("Ud ha reitardo con exito y transferido a su cuenta corriente")
                        print("Su nuevo saldo en la cuenta corriente es: " + str(ctaCte))
                        print("Su nuevo saldo en la cuenta ahorro es: " + str(ahorro))
                        decision = "0"
                    else:
                        if decision == '5':
                            print("-------------SALIR----------------")
                            respuesta = input("Quieres Salir? [SI][NO]: ")
                            if respuesta == "SI" or respuesta == "Si" or respuesta == "si":
                                salir = True
                            else:
                                if respuesta == "NO" or respuesta == "No" or respuesta =="no":
                                    salir = False #variable de control
                                    decision = "0"  
                                    print("Volviendo al MENU principal... ")
                                    print("---------------------------------")
                        else:
                            #Codigo de error
                            print("-------------ERROR----------------") 
                            print("La variable de decision es erronea!")
                            print("------------------------------------") 
                            decision = "0"
print("|||||||||||||SALIR||||||||||||||")
print("Procediendo a salir del programa")
print("|||||||||||||||||||||||||||||||||")
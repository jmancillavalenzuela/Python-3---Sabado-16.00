#Cajero Automatico V2.0 / Pagar Cuentas

#Variables Iniciales 
ctaCte = 20
ahorro = 50
linea = 100

print("Qué operación quiere hacer: ") 
print ("1. Depositar fondos Cuenta Corriente.") #Solo efectivo
print ("2. Retirar fondos Cuenta Corriente.") # Retirar fondos 
print ("3. Depositar fondos Cuenta Ahorro.") #Extraer dinero de la Cta Cte y depositar a cta Ahorra
print ("4. Retirar fondos Cuenta Ahorro") ##Depostiar dinero de la Cta Cte y extraer a cta Ahorra

#VARIABLE SALIR, LINEA SOBREGIRO ! PROXIMA CLASE

decision = input("Seleccionar Opcion: ")

#Delacaracion de Variables para usuario *Manipulacion*
abono = ""
depAhorro = ""
retAhorro = ""
pagar = ""

while 1:
    if decision == '0':
        #Desplegar MENU
        print("-------------MENU----------------") 
        print("Qué operación quiere hacer: ") 
        print ("1. Depositar fondos Cuenta Corriente.") #Solo efectivo
        print ("2. Retirar fondos Cuenta Corriente.") # Retirar fondos 
        print ("3. Depositar fondos Cuenta Ahorro.") #Extraer dinero de la Cta Cte y depositar a cta Ahorra
        print ("4. Retirar fondos Cuenta Ahorro") ##Depostiar dinero de la Cta Cte y extraer a cta Ahorra
        decision = input("Seleccionar Opcion: ")
    else:   
        if decision == '1':
            print("Ud. va a realizar una operación de depósito")
            print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
            abono = input("Cuanto desea abonar: ")
            ctaCte =  int(ctaCte) + int(abono) #Resultado ACTUAL ctaCte
            print("Su nuevo saldo en su cuenta corriente es " + str(ctaCte))
            decision = "0"
        else: 
            if decision == '2':
                print("Ud. ha seleccionado pagar una deuda")
                print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
                pagar = input("Cuanto desea pagar: ")
                ctaCte = int(ctaCte) - int(pagar)
                print("usted ha pagado su deuda con exito")
                print("Su nuevo saldo en la cuenta corriente es: " + str(ctaCte))
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
                        #Codigo de error
                        print("-------------ERROR----------------") 
                        print("La variable de decision es erronea!")
                        print("------------------------------------") 
                        decision = "0"
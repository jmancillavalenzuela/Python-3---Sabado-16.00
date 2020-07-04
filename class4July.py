#Cajero Automatico / Pagar Cuentas

#Variables Iniciales 
ctaCte = 20
ahorro = 50
linea = 100

print("Qué operación quiere hacer: ") 
print ("1. depositar.")
print ("2. pagar.")
print ("3. ahorrar.")

decision = input("Seleccionar Opcion: ")

#Delacaracion de Variables para usuario *Manipulacion*
abono = ""
depAhorro = ""
pagar = ""

if decision == '1':
    print("Ud. va a realizar una operación de depósito")
    print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
    abono = input("Cuanto desea abonar: ")
    ctaCte =  int(ctaCte) + int(abono) #Resultado ACTUAL ctaCte
    print("Su nuevo saldo es " + str(ctaCte))
else: 
    if decision == '2':
        print("Ud. ha seleccionado pagar una deuda")
        print("Su saldo actual en la cuenta corriente es: " + str(ctaCte))
        pagar = input("Cuanto desea pagar: ")
        ctaCte = int(ctaCte) - int(pagar)
        print("usted ha pagado su deuda con exito")
        print("Su nuevo saldo en la cuenta corriente es: " + str(ctaCte))
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
        else:
            #Codigo de error
            print("La variable de desicion es erronea!")


# Cartelera

print("Bienvenido a TicketSeller")
print("Real Madrid vs Barcelona, 1300 c/u,indica la opcion 1")
print("Napoli vs Juventus, 1000 c/u, indica la opcion 2")
print("Bayern Munich vs Leipzig, 900 c/u, indica la opcion 3")
print("Toluca vs America, 700 c/u, indica la opcion 4")


opcion = int(input("¿Que partido quiere ver?, indique la opcion:   "))
n_boletos  = int(input("¿Cuantos boletos quieres?:    "))

#Funcion partidos 

def partidos(opcion):
        if opcion == 1:
            return n_boletos * 1300
    
        elif opcion == 2:
            return n_boletos * 1000

        elif opcion == 3:
            return n_boletos * 900
        
        elif opcion == 4:
            return n_boletos * 700

print("El monto a pagar es de:", partidos(opcion))

opcion2 = input("¿Desea entradas para otro partido?:     ")

# While (bucle) - conidicionales

while opcion2 == "si":
    opcion2 = int(input("¿Que partido quiere ver?, indique la opcion:   "))
    n_boletos2  = int(input("¿Cuantos boletos quieres?:    "))

    def partidos2(opcion2):
        
        if opcion2 == 1:
            n_boletos2 * 1300
            return n_boletos2 * 1300
    
        elif opcion2 == 2:
            return n_boletos2 * 1000

        elif opcion2 == 3:
            return n_boletos2 * 900
        
        elif opcion2 == 4:
            return n_boletos2 * 700
        
    total = partidos(opcion) + partidos2(opcion2)

    print(total)
    
    opcion2 = input("¿Desea entradas para otro partido?:     ")
    
else:
    print("Ok, continuamos con su compra")


print("Somos accesibles a ustedes en su forma de pago")
n = input("su forma de pago sera con tarjeta?   ")

lista = ["banamex","bancomer","hsbc","scotiabank"]


if n == "si":
        
        print("solo aceptamos estas tarjetas: ",lista)
else:
        print("ok continuamos con su compra")










        



        
                
        

                  

        

        

 

                
                    




        

        
        
        
    
    
    









        
        
        

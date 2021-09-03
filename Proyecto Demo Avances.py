
opcion = int(input())

def partido1(n_boletos):

    return n_boletos * 1300

def partido2(n_boletos2):
    
    return n_boletos2 * 1000

def partido3(n_boletos3):

    return n_boletos3 * 900

def partido4(n_boletos4):

    return n_boletos4 * 700



   
if(opcion == 1):
    n_boletos  = float(input("Cuantos boletos quieres:    "))
    print(partido1(n_boletos))
elif(opcion == 2):
    n_boletos2  = int(input("Cuantos boletos quieres:    "))
    print(partido2(n_boletos2))
elif(opcion == 3):
    n_boletos3  = int(input("Cuantos boletos quieres:    "))
    print(partido3(n_boletos3))
elif(opcion == 4):
    n_boletos4  = int(input("Cuantos boletos quieres:    "))
    print(partido4(n_boletos4))









#Hoja de trabajo Python C

#Metodo

def adivinar(intento):
    Lector=input("¿De qué color es la fruta? \n")
    if Lector=="naranja":
        print("Felicidades, ganaste.")
    else:
        if intento<3:
            print("Fallaste, intentálo de nuevo.")
            intento+=1
            adivinar(intento)
        else:
            print("Ya no hay mas intentos. Perdiste")


adivinar(1)
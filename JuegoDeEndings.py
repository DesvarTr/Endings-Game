#Holaxd, Realizado por Gonzalo Montezuma

def VALIDACION(Opcioncilla):

    if Opcioncilla == "Z" or Opcioncilla == "X":

        pass

    else:
        print("ASEGURATE DE INGRESAR UNA OPCIÓN VÁLIDA\n")
        Opcioncilla = input("Intentalo de nuevo! (Z) / (X) ").upper()
        VALIDACION(Opcioncilla)

print("""\nAyer fue una noche lluviosa y afortunadamente tuviste una noche de sueño tranquila...
es martes, no tienes mucho que hacer, después de todo estás de vacaciones y puedes usar tu tiempo a gusto.
      
Extrañamente... te encuentras en un pequeño dilema, ¿deberías ir al gimnasio o de visita a un amigo?
      
PARA SELECCIONAR, ESCRIBE LA OPCIÓN QUE DESEES Y PRESIONA ENTER""")

Opcion1 = input("\nIr al gimnasio (Z) / Visitar a un amigo (X) ").upper()

VALIDACION(Opcion1)
print(Opcion1,"JAJAJJA")

if Opcion1 == "Z":
    print("De camino al gimnasio ")

elif Opcion1 == "X":
    print("""Sales en tu vehículo, ya que su casa no está muy cerca... el viaje será largo, posiblemente te tome 30 minutos
y tienes dos rutas por las cuales ir, talvez una de ellas sea más corta.""")
    
    OpcionX1 = input("\nTomar la ruta convencional (Z) / Tomar la ruta desolada (X) ").upper()
    VALIDACION(OpcionX1)

    if OpcionX1 == "X":
        print("""Por la ruta desolada, simplemente continúas tu camino tranquilamente, pero te quedas a medio camino sin gas
ahora deberás encontrar una manera de recargar tu tanque o avanzar a pie, tu vehículo es una moto así que no será tan dificil
caminar con el.""")
        
        OpcionX2 = input("\nCaminar a través del bosque (Z) / Caminar siguiendo la ruta (X) ").upper()
        VALIDACION(OpcionX2)

        if OpcionX2:
            print("")

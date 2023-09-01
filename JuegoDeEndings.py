#Holaxd, Realizado por Gonzalo Montezuma

def VALIDACION(Opcioncilla):

    if Opcioncilla == "Z" or Opcioncilla == "X":
        return Opcioncilla

    else:
        print("ASEGURATE DE INGRESAR UNA OPCIÓN VÁLIDA\n")
        Opcioncilla = input("Intentalo de nuevo! (Z) / (X) ").upper()
        return VALIDACION(Opcioncilla)

print("""\nAyer fue una noche lluviosa y afortunadamente tuviste una noche de sueño tranquila...
es martes, no tienes mucho que hacer, después de todo estás de vacaciones y puedes usar tu tiempo a gusto.
      
Extrañamente... te encuentras en un pequeño dilema, ¿deberías ir al gimnasio o de visita a un amigo?
      
PARA SELECCIONAR, ESCRIBE LA OPCIÓN QUE DESEES Y PRESIONA ENTER""")

Opcion1 = input("\nIr al gimnasio (Z) / Visitar a un amigo (X) ").upper()
Opcion1 = VALIDACION(Opcion1)

print(Opcion1,"JAJAJJA")

if Opcion1 == "Z":
    print("De camino al gimnasio ")

elif Opcion1 == "X":
    print("""Sales en tu vehículo, ya que su casa no está muy cerca... el viaje será largo, posiblemente te tome 30 minutos
y tienes dos rutas por las cuales ir, talvez una de ellas sea más corta.""")
    
    OpcionX1 = input("\nTomar la ruta convencional (Z) / Tomar la ruta desolada (X) ").upper()
    OpcionX1 = VALIDACION(OpcionX1)

    if OpcionX1 == "X":
        print("""Por la ruta desolada, simplemente continúas tu camino tranquilamente, pero te quedas a medio camino sin gas
ahora deberás encontrar una manera de recargar tu tanque o avanzar a pie, tu vehículo es una moto así que no será tan dificil
caminar con el.""")
        
        OpcionX2 = input("\nCaminar a través del bosque (Z) / Caminar siguiendo la ruta (X) ").upper()
        OpcionX2 = VALIDACION(OpcionX2)

        if OpcionX2 == "X":
            print("""Caminaste tanto que tienes mucha sed, no hay ningún tipo de fuente de agua cerca. No estas perdido, eso es algo
relativamente bueno, igualmente faltan unicamente 2km por recorrer para llegar a la gasolinera...
                  
Han pasado 30 minutos y ya no dás más, tus brazos están muy cansados y no sabes que deberías hacer, el dilema hace que te quedes
sentado esperando a ver que sucede, recargando energías.""")
            
            OpcionX3 = input("\nDejar el vehículo atrás (Z) / Seguir con el vehículo (X) ").upper()
            OpcionX3 = VALIDACION(OpcionX3)

            if OpcionX3 == "X":
                
                print("""Dió la noche, no has comido por tanto tiempo que ya no tienes energías, la única planta cerca es la
hiedra venenosa. Decides tomarla como último recurso. Fue una terrible idea.
                      
BAD ENDING: HAMBRE Y SED""")
                
            elif OpcionX3 == "Z":

                print("""Has avanzado hasta llegar a la gasolinera, tienes poco dinero y decides gastarlo en agua, igualmente ya estás
en la ciudad, lamentablemente eso no va a hacer que tu vehículo vuelva a ti...""")

                OpcionX4 =  input("\nRegresar por el vehículo (Z) / Seguir hacia la ciudad (X) ").upper()
                OpcionX4 = VALIDACION(OpcionX4)
            
                if OpcionX4 == "Z":

                    print("""Regresaste por el vehículo, pero esta vez por el bosque para llegar rápido y aprovechar la poca
agua que te queda, de la nada aparece una jauría de lobos de los cuales debes correr, y corres con todas tus energías
sin escapatoria, peleas con ellos y los vences relativamente fácil, pero por ir corriendo perdiste tu rumbo, ahora quedaste
atrapado en una zona del bosque sin nadie habitarlo, aún así es posible volver te tomará muchos más días...
                          
LOST ENDING: TE PERDISTE, AHORA TU DÍA Y HA PASADO Y NO PUDISTE HACER NADA MAS QUE BUSCAR UN REGRESO""")
                
                elif OpcionX4 == "X":

                    print("""La ciudad prece ser la equivocda, la ciudad a la que llegaste no es en la que vive tu amigo. Visitas
su casa y una señora amablemente te explica que siempre ha sido su casa ahí y que nunca llegó a vivir nadie joven por el lugar, ya
que el vecindario es bien conocido por alojar únicamente a gente mayor, ¿que pasó? Te ves demasiado confundido, no fue un error tuyo
claramente te había dado su dirección y estabas en el lugar indicado. Aún así le pides a la señora que te ayude y ver si te puede dejar
en casa, y de ser posible si está dispuesta a ir por tu vehículo. Ella acepta.

RARE ENDING: LA ESQUIZOFRENIA HIZO DE LAS SULLAS... PERO LOGRASTE SOLUCIONARLO""")

        elif OpcionX2 == "Z":

            print("""Caminaste dejando el vehículo atrás, no será un gran problema tampoco, pero de la misma forma tendrás que
distribuír bien tu energía para no cansarte tan rápidamente. Mientras más te adentras en el bosque más raro se pone el ambiente,
se siente muy extraño""")



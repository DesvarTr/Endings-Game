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
    print("""De camino al gimnasio te das cuenta que no está abierto, de hecho, al darte cuenta de eso vas a dar unas vueltas por
la pequeña ciudad, pero todo parece estar cerrado, talvez no te enteraste que habría una festividad este día. Vuelves rápidamente
a casa a ver que sucede. Lo peor, algo que nunca pudiste haber imaginado está sucediendo, en el mundo se liberó un virus, que
consigo causa que los muertos revivan, tengan comportamientos caníbales, y algunos registros apuntan que ya son capaces de colaborar
entre ellos para dominar el planeta. Algo está ocurriendo... un apocalipsis zombi.""")
    
    OpcionZ1 = input("\nSalir inmediatamente en busca de algún grupo organizado (Z) / Esconderse y buscar proviciones (X) ").upper()
    OpcionZ1 = VALIDACION(OpcionZ1)

    if OpcionZ1 == "Z":
        print("""Decides salir de casa y empezar a buscar cualquier indicio de vida humana, no encuentras nada cerca, y con tu
vehículo te vas fuera de la ciudad en busca de algún grupo de personas que estén preparandose para el apocalipsis, para tu mala suerte
en la dirección que fuiste te encontraste con una ciudad completamente zombificada, así que te ves obligado a regresar.""")

        Continuacion = True

    if OpcionZ1 == "X" or Continuacion:

        if Continuacion:
            print("")

        print("""Debes buscar todas las cosas necesarias para tu supervivcencia, comida, agua, herramientas y alguna manera de defenderte
así que vas al centro comercial más cercano, gracias a dios se encuentra totalmente abandonado, y si bien se llevaron multiples cosas
en su mayoría todo sigue ahí. Te llevas un pickup junto con una carga masiva de ropa, y empiezas a trasladar todo a tu casa. A la vez
haces un comunicado por internet de lo que sucede, y si alguien está cerca que es bienvenido y mejor si está dispuesto a ayudar.

LOS ZOMBIES SE ACERCAN""")
        
    OpcionZ2 = input("\nConstruir una base (Z) / Seguir manejando con muchas proviciones (X) ").upper()
    OpcionZ2 = VALIDACION(OpcionZ2)

    if OpcionZ2 == "Z":
        print("""Empiezas a construir tu base que conecta casi todas las casas del vecindario a través de ductos, no fue tan difícil
lograrlo pero si tomó tiempo, luego de un tiempo te dedicas a formar un sistema de defensa y a esparcir armas por los lugares donde
más pasarás tiempo en caso de una emergencia. La primera holeada de zombies aparece, pero pasas desapercibido.""")
        
        OpcionZ3 = input("\nEsperar mientras ves las noticias (Z) / Salir por alimento (X) ").upper()
        OpcionZ3 = VALIDACION(OpcionZ3)

        if OpcionZ3 == "Z":
            print("""En la televisión vez de que cada vez el mundo está mas en ruinas, aún así hay 2 organizaciones que se están
dedicando a erradicar todos los zombis posibles, y si esperas el tiempo suficiente, todos estos se van a descomponer y no quedarán
más, por lo que sobrevivirás y cuando pase el apocalipsis podrás vivir en el mundo normalmente. Escuchas unos fuertes ruidos en la
entrada de tu base, esta vez quieren saquear todo.""")
            
            OpcionZ4 = input("\nCamuflarse (Z) / Defenderse (X) ").upper()
            OpcionZ4 = VALIDACION(OpcionZ4)

            if OpcionZ4 == "Z":
                print("""Te camuflas, no sucede nada por mucho tiempo, escuchas por horas los incesantes sonidos, rugidos
golpes y daños que provocan los zombies, y esperas a que al fin se vayan. Luego de alrededor de 1 día y medio, los zombies pasan
y ya no están ahí, vuelves a encender el televisor, que a duras penas funciona. Pero ves que justamente los investigadores dicen que
no queda ni un solo zombi en tu país, lograste salvarte, aunque tendrás que desinfectar absolutamente todo, y vivir totalmente
aislado, hasta que el grupo mundial contra los zombies visite tu país.
                      
GOOD ENDING: SOBREVIVISTE AL ARMAGEDÓN""")
                
            elif OpcionZ4 == "X":
                print("""Sales a matar a muchos zombis, tus armas son efectivas, y tu bobina vuelve cenizas casi instantáneamente a todos
pero hay un problema reciente, ahora los zombies parecen mucho más resistentes, sales de la casa y buscas un espacio abierto en el cual te puedes
defender a distancia. Matas a muchísimos de ellos, pero algunos aún llegan a tocarte, eso no representa un riesgo, pero ves como
han mutado, y ahora tienen una fuerza de agarre impresionante. Mientras peleabas con dos gigantes, un astuto flacucho logró agarrarte
con todas sus fuerzas, y aunque te libraste de el, solo fue una distracción. Te rodearon completamente.
                      
BAD ENDING: TE CONVERTISTE EN ZOMBI""")
                
        elif OpcionZ3 == "X":
            print("""Sales a un supermercado en busca de más provisiones, pero los zombies empiezan a entrar a tu base en ese momento.
Te ves forzado a refugiarte en el supermercado, pero mutantes entran con fuerza, y rompen absolutamente todo lo que encuentran a su paso.
Posteriormente, proceden a seguirte, tu logras defenderte de muchos de ellos, pero los ultimos parecen improbables. Por su aumento anabólico
excesivo, es casi imposible penetrarlos con balas, y aunque la piel absorbe la electricidad, la usan a su favor y la logran catalizar
en sus dedos para usarlas como armas.
                  
DEATH ENDING: NO TE CONVERTISTE EN ZOMBIE, PERO MORISTE A CAUSA DE SUS ATAQUES""")
            
    elif OpcionZ2 == "X":
        print("""Manejas fuera de la ciudad con todas las proviciones que puedes, y encuentras una prisión abandonada, te decides quedar
ya que esta aporta protección y seguridad máxima, aparte que el acceso por el momento es ilimitado y puedes utilizar celdas como laboratorios.
Una holeada de zombies ha entrado a la ciudad, y a los alrededores.""")

    OpcionZ5 = input("\nCapturar zombies para investigar (Z) / Esconderse y buscar proviciones (X) ").upper()
    OpcionZ5 = VALIDACION(OpcionZ5)

    if OpcionZ5 == "Z":
        print("""Sorprendentemente tu idea sale bien, logras encerrrar zombies en celdas de prisión, y buscas cambios conforme
los vas capturando, notas que algunos poseen mutaciones que otros no, como lo son el aumento anabólico y la fuerza de agarre.
Poco a poco vas investigando más a fondo, al punto que te vuelves loco por tu investigación. A cierto punto pierdes totalmente la cordura
te das cuenta que ser un zombie es mucho mejor que ser un humano, y sin pensarlo. Voluntariamente te expones a un contagio.

MAD ENDING: TE VOLVISTE LOCO, AHORA ERES UN ZOMBI QUE ALGUNA VEZ FUE UN CIENTÍFICO INDEPENDIENTE""")
        
    elif OpcionZ5 == "X":
        print("""Te escondes bien en la prisión, pero hay muy poca comida restante, decides que tendrás que arriesgarte y volver
a la ciudad en busca de comida, pero de camino encuentras a un grupo de zombies que increíblemente ha desarrollado la capacidad
de manejar carros casi a la perfección, los zombies te siguen por un lado, y rápidamente se vuelve una carrera, no, una pelea
automovilística. El momento es frenético, el piloto del auto zombie solo espera la oportunidad de chocar, o que algun zombi se lance
y pueda infectarte, en un segundo, un helicoptero de las fuerzas aliadas pasa por encima del carro, pero esto causa una catástrofe.
La luz te encandila por un segundo, el cual aprovecharon los zombies para chocarte, tu auto queda inservible, y sorprendentemente sobrevives.
Al final, te das cuenta que diversos metales quedaron incrustados en tu pecho por el accidente, los zombies murieron casi inmediatamente.
Ya no te queda más que esperar a una muerte lenta por desangramiento.
              
RACING ENDING: EL CHOQUE TE DEJÓ HERIDO, AHORA MORIRÁS POR DESANGRAMIENTO EN POCAS HORAS""")

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
se siente muy extraño y sientes la presencia de una entidad anómala""")
        
            OpcionX5 = input("\nEsperar en un arbusto (Z) / Seguir el camino (X) ").upper()
            OpcionX5 = VALIDACION(OpcionX5)

            if OpcionX5 == "X":

                print("""Sigues el camino ignorando el sonido, pero mientras avanzas el sonido aumenta, se escucha en todas las
direcciones asi que no puedes saber con certeza de que dirección viene, o qué lo produce. Eventualmente sigues caminando y te en
cuentras una figura humanoide extraña de color blanco, asustado, intentas rodearlo. Pero este emite un grito fuertísimo y aterrador.
Naturalmente volteas a ver, y ves su cara. La figura empieza a correr hacia ti sin que nada lo detenga, paralizado, solo esperas
tu fin sin poder hacer nada.

096 ENDING: NO DEBISTE VER SU ROSTRO""")

            elif OpcionX5 == "Z":
            
                print("""En el arbusto ves como una figura extraña pasa por el lugar, pero esta se va lentamente, y los sonidos
se pierden y se alejan, te pudiste salvar de esta... Ya en la ciudad buscas la casa de tu amigo, y aunque te toma un tiempo logras
encontrarla con relativa facilidad, el te recibe y luego van juntos por tu vehículo, al estar de regreso ya está atardeciendo
ambos disfrutan de lo que resta del día y sin problemas graves.
                      
GOOD ENDING: TU PLAN SALIÓ BIEN""")

    elif OpcionX1 == "Z":
        print("""La ruta convencional te toma mucho más tiempo por recorrer, pero no es un gran problema, a mitad de camino
te quedas sin gasolina y encuentras una gasolinera cercana para seguir normalmente, llegas a la ciudad que buscabas y al llegar
a casa de tu amigo piensan en que podrían hacer, talvez vendría bien algo de exploración a la parte trasera del vecindario.""")
        
        OpcionX2 = input("\nIr a la cueva (Z) / Ir al árbol antiguo (X) ").upper()
        OpcionX2 = VALIDACION(OpcionX2)

        if OpcionX2 == "Z":
            print("""Ambos van caminando a una cueva que había cerca del lugar, la cueva está bastante oscura, así que llevan
una luz bastante potente que les permite ver profundo, encuentran distintas rocas semi preciosas y preciosas, por lo que inclusive
llegan a pensar en que si en un futuro podrían iniciar su negocio alrededor de eso.""")
            
            OpcionX3 = input("\nIr hasta lo más profundo (Z) / Quedarse en la generación de piedras preciosas (X) ").upper()
            OpcionX3 = VALIDACION(OpcionX3)

            if OpcionX3 == "Z":
                print("""Siguieron yendo a lo más profundo de la cueva, y encontraron un extraño cristal sobre una piedra de
granito, se ve muy brillante que incluso emana luz de él. Deciden intentar llevarselo pero al hacer contacto, instantáneamente
se empiezan a convertir en cristal, ambos terminan cubiertos del misterioro cristal, y sin escapatoria terminan ambos explotando por
la inmensa presión que generó la concentración de todo el cristal en todo su cuerpo.
                      
409 ENGING: SE CONTAGIARON.""")
                
            elif OpcionX3 == "X":
                print("""Al quedarse en la cueva, estuvieron muy seguros y fueron capaces de llevarse algunas muestras de las piedras
para investigar un poco más acerca de ellas y si son factibles para generar comercio a partir de ellas, logran salir de la cueva sin problemas
y aunque ya es muy tarde, ambos piensan que si realmente es prometedor el mercado, podrán abandonar su trabajo y vivir de ello.

STONKS ENDING: CON SUERTE, NUNCA TENDRÁN QUE PISAR OTRA OFICINA""")
                
        elif OpcionX2 == "X":
            print("""Ambos se dirigen a un arbol extraño en el bosque del lugar, se ve muy peligroso y está casi todo cubierto
de telarañas en su exterior, en su interior se ven unas lianas que aparentan llegar hasta al fondo del lugar. Ambos bajan cuidadosamente
esperando encontrar algo que valga la pena documentar. Pero a lo lejos ven unas arañas que parecen ser venenosas, se van por uno de
los caminos vacíos, pero fue una mala idea, las arañas estaban justo en el techo, por lo que no pudieron verlas, eran demasiado
gigantes como para matarlas de un pisotón. Quedaron totalmente atrapados, como las presas de las arañas.
                  
VENOMOUS ENDING: LAS ARAÑAS VENENOSAS LOS DEVORARON POR INVADIR SU NIDO""")
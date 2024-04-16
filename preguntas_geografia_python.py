preguntas_geografía={"¿Cuál es la montaña más alta de España?": "Teide",
                    "¿El mar muerto es realmente un mar?":"No",
                    "¿Qué continente es el más poblado?":"Asia",
                    "¿Qué río pasa por más países?":"Danubio",
                    "¿Cuál es el país más pequeño del mundo?":"Ciudad del Vaticano",
                    "¿Cuántos océanos hay en la Tierra? (Inserta un número)" : "5",
                    "¿Qué río pasa por París?" : "Sena",
                    "¿Cuál es el río más largo de España?" : "Tajo",
                    "¿Qué ocupa más superficie, el agua o los continentes? (Escribe 'el agua' o 'los continentes')" : "El agua",
                    "¿Cuál es el continente más seco del planeta? (escribe sin acentos)": "Antartida",
                    "¿Cuál es la isla más grande del mundo?" : "Groenlandia",
                    "¿Cual es la capital de Argentina?" : "Buenos Aires"}

#Importamos la librería random para que podamos dar resultados aleatorios más adelante:
import random

# Iniciamos juego dando la bienvenida y explicando las reglas del juego.
print("WELCOME! En este juego de preguntas y respuestas de geografía, pondrás a prueba tus conocimientos. \n\n ¡Piensa bien cada respuesta! La partida terminará cuando alcances 3 fallos. \n Para ganar, deberás acertar 5 preguntas. \n Fácil, ¿no? \n")
print("*"*60)
print("¿Estás preparado/a?")
start = input("Pulsa cualquier letra para empezar a jugar.")
pass
print("START")
print("*"*30)

# Creamos una funcion para seleccionar y ofrecer a la persona usuaria una pregunta aleatoria de nuestro diccionario, sin que esta se repita.
def juego():

#Convertimos las keys en una lista para poder seleccionar solo las claves.
    preguntas = list(preguntas_geografía.keys()) 
    preguntas_hechas = []

# Creamos dos variables que nos servirán para contar las respuestas correctas y los fallos por partida. 
    respuestas_correctas=0
    fallos=0

    while len(preguntas_hechas) <= len(preguntas_geografía):
            pregunta_aleatoria= random.choice(preguntas)
            respuesta_usuario= input(pregunta_aleatoria).lower()


            if pregunta_aleatoria not in preguntas_hechas:
                print(f"{pregunta_aleatoria} \n")
                preguntas_hechas.append(pregunta_aleatoria)
                respuestas = preguntas_geografía[pregunta_aleatoria]
                preguntas.remove(pregunta_aleatoria)
            
                if respuesta_usuario == respuestas.lower():
                    print(f"Tu respuesta es {respuesta_usuario}")
                    print("¡Has acertado! \n")
                    respuestas_correctas += 1
                    print(f"LLevas {respuestas_correctas} aciertos.")
                    print("<3"*40)
                    

                    if respuestas_correctas == 5:
                        print("\n")
                        print("*"*60)
                        print("ENHORABUENA \n ¡¡HAS GANADO EL JUEGO!!")
                        break

                else:
                    fallos += 1
                    print(f"Tu respuesta es {respuesta_usuario}")
                    print(f"¡Ups! Has fallado. La respuesta correcta es {respuestas}.\n") 
                    print(f"¡Cuidado! Llevas {fallos} fallos.")
                    print("-"*60) 

                    if fallos==3:
                        print("\n")
                        print("*"*60)
                        print("¡GAME OVER! \n HAS FALLADO 3 VECES.\n\n\n\n")
                        break

            else:
                print("No quedan más preguntas en el juego!")
                break

    return juego

juego()

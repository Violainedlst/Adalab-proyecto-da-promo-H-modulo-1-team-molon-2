# importamos la función random
import random

# definimos el número de puntos objetivo
puntos_objetivo = 3

# definimos las opciones válidas
opciones = ('piedra', 'papel', 'tijera')

# creamos un marcador para sumar los puntos que van sacando los jugadores en cada ronda
puntos_usuario = 0
puntos_ordenador = 0

# creamos la variable 'rondas', que se irá sumando
ronda = 1

# imprimimos las instrucciones
print(f'💥\033[1mPiedra, papel, tijera\033[0m💥\n\n- Piedra🪨 vence a tijera✂️.\n- Tijera✂️ vence a papel🧻.\n- Papel🧻 vence a piedra🪨.\n- Se obtiene un punto por cada ronda ganada1️⃣.\n- Gana el juego quien haya conseguido 3 puntos.🏆')

while True:
    
    # queremos que, al principio de cada ronda, imprima qué ronda estamos jugando y cuántos puntos lleva cada jugador
    print('\n**********\n')
    print(f'Ronda: {ronda}')
    print(f'La persona jugadora lleva {puntos_usuario} puntos')
    print(f'El ordenador lleva {puntos_ordenador}\n')

    # definimos todo lo relativo a la elección del usuario
    eleccion_usuario = input("Elige entre piedra, papel o tijera:")
    # pasamos la opción del usuario a minúsculas por si se equivoca al escribir
    eleccion_usuario = eleccion_usuario.lower()
    if not eleccion_usuario in opciones:
        print("Opción inválida. Vuelve a intentarlo")
        continue # esto hace que si la elección del usuario es una palabra no válida, vuelva a empezar (que no ejecute todo lo que hay abajo)

    # definimos todo lo relativo a la elección del ordenador: que elija aleatoriamente entre las opciones
    eleccion_ordenador =  random.choice(opciones)

    print(f'Elección de la persona jugadora: {eleccion_usuario}')
    print(f'Elección del ordenador: {eleccion_ordenador}\n')

    # si usuario y ordenador coinciden hay empate
    if eleccion_usuario == eleccion_ordenador:
        print("Empate😑")

    # opciones si el usuario saca piedra
    elif eleccion_usuario == 'piedra':
        if eleccion_ordenador == 'tijera': #si el usuario saca piedra y el ordenador tijera, gana el usuario
            print('Piedra🪨 gana a tijera✂️')
            print('¡Gana La persona jugadora!🧠')
            puntos_usuario += 1
        # la única opción restante es que el ordenador saque papel (gana el ordenador)
        else:
            print('Papel🧻 gana a piedra🪨')
            print('¡Gana el ordenador!💻')
            puntos_ordenador += 1

    # opciones si el usuario saca papel
    elif eleccion_usuario == 'papel':
        if eleccion_ordenador == 'piedra': # si el usuario saca paple y el ordenador piedra, gana el usuario
            print('Papel🧻 gana a piedra🪨')
            print('¡Gana la persona jugadora!🧠')
            puntos_usuario += 1
        # la única opción restante es que el ordenador saque tijera
        else:
            print('Tijera✂️ gana a papel🧻')
            print('¡Gana el ordenador!💻')
            puntos_ordenador += 1

    #opciones si el usuario saca tijeras
    elif eleccion_usuario == 'tijera':
        if eleccion_ordenador == 'papel':# si el usuario saca tijera y el ordenador papel, gana el usuario
            print('Tijera✂️ gana a papel🧻')
            print('¡Gana la persona jugadora!🧠')
            puntos_usuario += 1
        #la única opción restante es que el ordenador saque piedra
        else:
            print('Piedra🪨 gana a tijera✂️')
            print('¡Gana el ordenador!💻')
            puntos_ordenador += 1

    if puntos_usuario == puntos_objetivo:
        print('\nAnd the absolute winner is: \n🎆¡La persona jugadora!🧠 🥇')
        break

    if puntos_ordenador == puntos_objetivo:
        print('\nAnd the absolute winner is: \n👎¡El ordenador!💻 👎')
        break

    ronda += 1
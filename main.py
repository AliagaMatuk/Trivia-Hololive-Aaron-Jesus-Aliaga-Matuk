#Imports
import time

# Colores
"""BLACK = '\033[30m' RED = '\033[31m' GREEN = '\033[32m' YELLOW = '\033[33m' BLUE = '\033[34m' CYAN = '\033[36m' RESET = '\033[39m'"""

# Variables/texto
intro = "\nBienvenido a mi trivia sobre la empresa de Vtubers: Hololive\n"
presentacion = "Ingresa tu nombre: "
intro2 = "\n" + "Pondremos a prueba tus conocimientos"
trivia = "\n" + "Responde las siguientes preguntas escribiendo el número de la alternativa y presionando 'Enter' para enviar la respuesta \n"

# Variables/preguntas & respuestas
pregunta_1 = "¿Quién fue el primer talento en unirse a Hololive?"
opciones_1 = "\n1) Roboco-san\n2) Tokino Sora\n3) Hoshimachi Suisei\n4) Sakura Miko"
respuesta_1 = 2
pregunta_2 = "¿Cuál es la especialidad de Shishiro Botan?"
opciones_2 = "\n1) RPG\n2) MMORPG\n3) MOBA\n4) FPS"
respuesta_2 = 4
pregunta_3 = "¿Cuál es el apodo más usado de Hoshimachi Suisei en juegos?"
opciones_3 = "\n1) Suiz\n2) Sui-chan\n3) Suicopath\n4) Stellar"
respuesta_3 = 3
pregunta_4 = "¿Quién le puso el apodo a YAGOO?"
opciones_4 = "\n1) Oozora Subaru\n2) Inugami Korone\n3) Shirakami Fubuki\n4) Uruha Rushia"
respuesta_4 = 1
# Arreglos
preguntas = [pregunta_1, pregunta_2, pregunta_3, pregunta_4]
opciones = [opciones_1, opciones_2, opciones_3, opciones_4]
respuestas = [respuesta_1, respuesta_2, respuesta_3, respuesta_4]
# Otras Variables
cantidadPreguntas = len(preguntas)
puntaje = 0
valor = 0
nombre = ""
noError = True
iniciarTrivia = True
intentos = 1

#===================================================================================
# Código
#===================================================================================
nombre = input(presentacion)
while iniciarTrivia:
    #Presentación:
    print(intro, "Participante:", nombre, "\nNúmero de intentos: ", intentos)
    print(intro2)
    print(trivia)

    # Bucle para la trivia
    i = 0
    while i in range(cantidadPreguntas):
        #Imprimir preguntas y opciones solo si se dio una respuesta válida:
        if noError:
            print(preguntas[i], opciones[i])
        #Try para validar que la respuesta sea un número entero
        try:
            valor = int(input("\nLa respuesta es: "))
            #While para validar que la respuesta se encuentre entre las opciones
            while valor not in (1, 2, 3, 4):
                valor = int(
                    input(
                        "Debes responder un número válido, ingrese nuevamente la respuesta: "
                    ))
            if valor == respuestas[i]:
                print("\n¡Correcto!\n")
                puntaje += 5
            else:
                print("\nIncorrecto.\n")
                puntaje -= 2
            noError = True
            i += 1
            print("Su puntaje hasta el momento es de: ", puntaje, "/20\n")
            print("Se le daran 5 segundos de descanso hasta la siguiente pregunta\n")
            time.sleep(5)  #Espera de 5 segundos
        except ValueError:
            print("¡La respuesta debe ser expresada en números, intente de nuevo!")
            noError = False
    #End While
    print("¡Felicidades! Su puntaje final es de: ", puntaje, "/20\n")

    repetirTrivia = input(
        "¿Deseas repetir una vez más la trivia?\n¿Sí o No?\n")
    if repetirTrivia == "Sí" or repetirTrivia == "Si" or repetirTrivia == "si":
        intentos += 1
        puntaje = 0
    else:
        break

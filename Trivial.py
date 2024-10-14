import random
import time
import os
num_jugadores=int(input('cuantos jugadores van a jugar: '))#num de jugadores que van a jugar
jugadores=[]#creamos una lista vacia donde pondremos los dicionarios que creemos
'''
En este bucle for que tiene complejidad N creamos los jugadores que van ajugar al juego 
de trivia: creando el nombre que nos va ha permitir diferenciar entre cada
jugador. Y los aciertos y fallos que estan vacion que se van a sumar mas tarde en 
este algoritmo 
'''
for i in range(1,num_jugadores+1):
    jugado = {
        "nombre":input(f"Nombre jugador {i}: "),
        "fallos": 0,
        "aciertos": 0
        }
    jugadores.append(jugado)
time.sleep(1)
os.system('cls')
time.sleep(1)
'''
Aqui esta las preguntas que es una lista de dicionarios
con sus claves respectivas: enunciados respuestas y respuestas_correctas
'''
preguntas= [
    {
        "enunciado": "¿Cuál es el planeta más cercano al Sol?",
        "respuestas": ("A: Venus", "B: Tierra", "C: Mercurio", "D: Marte"),
        "respuesta_correcta": "C"
    },
    {
        "enunciado": "¿Quién escribió 'Cien años de soledad'?",
        "respuestas": ("A: Gabriel García Márquez", "B: Julio Cortázar", "C: Pablo Neruda", "D: Mario Vargas Llosa"),
        "respuesta_correcta": "A"
    },
    {
        "enunciado": "¿Cuál es el símbolo químico del hierro?",
        "respuestas": ("A: Fe", "B: H", "C: He", "D: Ir"),
        "respuesta_correcta": "A"
    },
    {
        "enunciado": "¿Qué continente es conocido como el 'continente negro'?",
        "respuestas": ("A: Asia", "B: África", "C: Europa", "D: América"),
        "respuesta_correcta": "B"
    },
    {
        "enunciado": "¿Quién fue el primer presidente de los Estados Unidos?",
        "respuestas": ("A: Abraham Lincoln", "B: George Washington", "C: Thomas Jefferson", "D: John Adams"),
        "respuesta_correcta": "B"
    },
    {
        "enunciado": "¿Cuál es la capital de Francia?",
        "respuestas": ("A: Madrid", "B: Berlín", "C: Roma", "D: París"),
        "respuesta_correcta": "D"
    },
    {
        "enunciado": "¿Qué órgano del cuerpo humano es responsable de bombear sangre?",
        "respuestas": ("A: Hígado", "B: Pulmón", "C: Corazón", "D: Riñón"),
        "respuesta_correcta": "C"
    },
    {
        "enunciado": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "respuestas": ("A: 1935", "B: 1939", "C: 1941", "D: 1945"),
        "respuesta_correcta": "B"
    },
    {
        "enunciado": "¿Cuál es el océano más profundo del mundo?",
        "respuestas": ("A: Océano Atlántico", "B: Océano Índico", "C: Océano Ártico", "D: Océano Pacífico"),
        "respuesta_correcta": "D"
    },
    {
        "enunciado": "¿Qué país inventó el sushi?",
        "respuestas": ("A: China", "B: Japón", "C: Corea", "D: Tailandia"),
        "respuesta_correcta": "B"
    }
]
random.shuffle(preguntas)
random.shuffle(preguntas['respuestas'])
'''
En este bucle pasamos por la lista de dicionarios de las preguntas
Tenendo un N de complejidad
'''
for pregunta in preguntas:
    print(pregunta['enunciado'])
    print(pregunta['respuestas'])
    '''
    En este bucle for vamos a a preguntar a cada jugador su respuesta de 
    las preguntas
    Otro N de complejidad
    '''
    for jugador in jugadores:
        answer_player=input(f"Respuesta de {jugador['nombre']}:\t")
        answer=answer_player.upper()

        if answer==pregunta['respuesta_correcta']:
            jugador['aciertos']+=1#aumenta los aciertos si el answer es el mismo que la respuesta_correcta

        else:
            jugador['fallos']+=1#aumentan los fallos si no es correcto
#mostrar aciertos y fallos
for jugador in jugadores:# un N de complejidad
    print(f"{jugador['nombre']} tuvo: \n{jugador['aciertos']} aciertos\n{jugador['fallos']} fallos")
'''
En esta funcion jugadores_ordenados ordenamos los jugadores por el numero de aciertos
pero de ascendiente a descendiente por eso reverse=True
'''
time.sleep(20)
os.system('cls')
jugadores_ordenados = sorted(jugadores, key=lambda jugador: jugador['aciertos'], reverse=True)

# Mostrar posiciones
for posicion, jugador in enumerate(jugadores_ordenados, start=1):# un N de complejidad
    print(f'{posicion}ª posición: es para el jugador: {jugador["nombre"]} con {jugador["aciertos"]} aciertos')
time.sleep(30)
os.system('cls')
print('\t>>>>>>>>>>GEME OVER<<<<<<<<<<<<<<<<<')
print('**************THANKS FOR PLAYIN************')







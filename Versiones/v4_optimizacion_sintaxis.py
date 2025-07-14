### Mejora 3 ###

import json
import requests as rq

url = 'https://v3.football.api-sports.io/'
headers = {
    'x-apisports-key': 'd1097185ee42e79bae3f876df5733904',
    'content-type': 'application/json'
}

def encontrar_equipos(url_personalizada) -> list:
    try:
        respuesta = rq.get(url_personalizada, headers=headers)
        respuesta.raise_for_status()
        datos = respuesta.json()
        lista_equipos_1 = []
        for team in datos['response']:
            id_equipo = team['team']['id']
            lista_equipos_1.append(id_equipo)
        del lista_equipos_1[1:]
        return lista_equipos_1
    except rq.exceptions.HTTPError as e:
        print(f'Error de HTTP: {e}')
    except rq.exceptions.RequestException as e:
        print(f'Error de conexion o de solicitud: {e}')

lista_equipos = []
for i in range(5):
    equipo = input('Ingrese un equipo: ')
    lista_equipos.append(equipo)

for equipo in lista_equipos:
    url_equipo = f'https://v3.football.api-sports.io/teams?search={equipo}'
    if equipo == lista_equipos[0]:
        id_equipo_1 = encontrar_equipos(url_personalizada=url_equipo)
    elif equipo == lista_equipos[1]:
        id_equipo_2 = encontrar_equipos(url_personalizada=url_equipo)
    elif equipo == lista_equipos[2]:
        id_equipo_3 = encontrar_equipos(url_personalizada=url_equipo)
    elif equipo == lista_equipos[3]:
        id_equipo_4 = encontrar_equipos(url_personalizada=url_equipo)
    elif equipo == lista_equipos[4]:
        id_equipo_5 = encontrar_equipos(url_personalizada=url_equipo)

def encontrar_jugadores(url_jugador) -> list:
    try:
        respuesta_jugador_1 = rq.get(url_jugador, headers=headers)
        respuesta_jugador_1.raise_for_status()
        datos_jugador_1 = respuesta_jugador_1.json()
        id_jugador_1_list = []
        for id in datos_jugador_1['response']:
            id_jugador_1 = id['player']['id']
            id_jugador_1_list.append(id_jugador_1)
        return id_jugador_1_list
    except rq.exceptions.HTTPError as e:
        print(f'Error de HTTP: {e}')
    except rq.exceptions.RequestException as e:
        print(f'Error de  conexion o de solicitud: {e}')

lista_ids_equipos = [id_equipo_1, id_equipo_2, id_equipo_3, id_equipo_4, id_equipo_5]

lista_jugadores = []
for i in range(5):
    jugador = input(f'Ingrese un jugador del {lista_equipos[i]}: ')
    lista_jugadores.append(jugador)

for num, jugador in enumerate(lista_jugadores):
    url_jugador = f'https://v3.football.api-sports.io/players?search={jugador}&team={lista_equipos[0 + num]}'
    if jugador == lista_jugadores[0]:
        id_jugador_1 = encontrar_jugadores(url_jugador)
    elif jugador == lista_jugadores[1]:
        id_jugador_2 = encontrar_jugadores(url_jugador)
    elif jugador == lista_jugadores[2]:
        id_jugador_3 = encontrar_jugadores(url_jugador)
    elif jugador == lista_jugadores[3]:
        id_jugador_4 = encontrar_jugadores(url_jugador)
    elif jugador == lista_jugadores[4]:
        id_jugador_5 = encontrar_jugadores(url_jugador)

print(id_jugador_1)
print(id_jugador_2)
print(id_jugador_3)
print(id_jugador_4)
print(id_jugador_5)
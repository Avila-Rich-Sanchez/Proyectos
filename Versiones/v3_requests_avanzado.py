### Mejora 2 ###

import json
from traceback import print_tb
import requests as rq

url = 'https://v3.football.api-sports.io/'
headers = {
    'x-apisports-key': 'd1097185ee42e79bae3f876df5733904',
    'content-type': 'application/json'
}

equipo_1 = input('Ingrese el nombre del equipo: ').title()

url_personalizada = f'https://v3.football.api-sports.io/teams?search={equipo_1}'
try:
    respuesta = rq.get(url_personalizada, headers=headers)
    respuesta.raise_for_status()
    datos = respuesta.json()
    texto_json = json.dumps(datos, indent=4)
    lista_equipos_1 = []
    for team in datos['response']:
        id_equipo = team['team']['id']
        lista_equipos_1.append(id_equipo)
    del lista_equipos_1[1:]
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de conexion o de solicitud: {e}')

print(lista_equipos_1)

equipo_2 = input('Ingrese el nombre del equipo: ').title()

url_personalizada = f'https://v3.football.api-sports.io/teams?search={equipo_2}'
try:
    respuesta = rq.get(url_personalizada, headers=headers)
    respuesta.raise_for_status()
    datos = respuesta.json()
    texto_json = json.dumps(datos, indent=4)
    lista_equipos_2 = []
    for team in datos['response']:
        id_equipo = team['team']['id']
        lista_equipos_2.append(id_equipo)
    del lista_equipos_2[1:]
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de conexion o de solicitud: {e}')


print(lista_equipos_2)

jugador_1 = input('Ingrese el nombre del jugador del primer equipo: ')
try:
    url_personalizada_jugador_1 = f'https://v3.football.api-sports.io/players?search={jugador_1}&team={lista_equipos_1[0]}'
    respuesta_jugador_1 = rq.get(url_personalizada_jugador_1, headers=headers)
    respuesta_jugador_1.raise_for_status()
    datos_jugador_1 = respuesta_jugador_1.json()
    texto_json_jugador_1 = json.dumps(datos_jugador_1)
    id_jugador_1_list = []
    for id in datos_jugador_1['response']:
        id_jugador_1 = id['player']['id']
        id_jugador_1_list.append(id_jugador_1)
    # del id_jugador_1_list[1:]
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de  conexion o de solicitud: {e}')

if not id_jugador_1_list:
    print('No se encontraron equipos.')
    exit()

print(id_jugador_1_list)


jugador_2 = input('Ingrese el nombre del jugador del primer equipo: ')
try:
    url_personalizada_jugador_2 = f'https://v3.football.api-sports.io/players?search={jugador_2}&team={lista_equipos_2[0]}'
    respuesta_jugador_2 = rq.get(url_personalizada_jugador_2, headers=headers)
    respuesta_jugador_2.raise_for_status()
    datos_jugador_2 = respuesta_jugador_2.json()
    texto_json_jugador_2 = json.dumps(datos_jugador_2)
    id_jugador_2_list = []
    for id in datos_jugador_2['response']:
        id_jugador_2 = id['player']['id']
        id_jugador_2_list.append(id_jugador_2)
    del id_jugador_2_list[1:]
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de  conexion o de solicitud: {e}')

if not id_jugador_2_list:
    print('No se encontraron equipos.')
    exit()

print(id_jugador_2_list)

try:
    url_transferencias_jugador_1 = f'https://v3.football.api-sports.io/transfers?player={id_jugador_1_list[0]}'
    respuesta_jugador_1 = rq.get(url_transferencias_jugador_1, headers=headers)
    respuesta_jugador_1.raise_for_status()
    datos_jugador_1 = respuesta_jugador_1.json()
    texto_json_jugador_1 = json.dumps(datos_jugador_1)
    equipos_jugador_1 = []
    for equipo in datos_jugador_1['response'][0]['transfers']:
        equipo_entrada = equipo['teams']['in']['name']
        equipo_salida = equipo['teams']['out']['name']
        tupla = [equipo_entrada, equipo_salida]
        equipos_jugador_1.extend(tupla)
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de  conexion o de solicitud: {e}')

equipos_jugador_1 = set(equipos_jugador_1)
print(equipos_jugador_1)

try:
    url_transferencias_jugador_2 = f'https://v3.football.api-sports.io/transfers?player={id_jugador_2_list[0]}'
    respuesta_jugador_2 = rq.get(url_transferencias_jugador_2, headers=headers)
    respuesta_jugador_2.raise_for_status()
    datos_jugador_2 = respuesta_jugador_2.json()
    texto_json_jugador_2 = json.dumps(datos_jugador_2)
    equipos_jugador_2 = []
    for equipo in datos_jugador_2['response'][0]['transfers']:
        equipo_entrada = equipo['teams']['in']['name']
        equipo_salida = equipo['teams']['out']['name']
        tupla = [equipo_entrada, equipo_salida]
        equipos_jugador_2.extend(tupla)
except rq.exceptions.HTTPError as e:
    print(f'Error de HTTP: {e}')
except rq.exceptions.RequestException as e:
    print(f'Error de  conexion o de solicitud: {e}')

equipos_jugador_2 = set(equipos_jugador_2)
print(equipos_jugador_2)

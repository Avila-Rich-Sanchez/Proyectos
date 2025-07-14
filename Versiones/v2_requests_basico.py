import json
import requests as rq

url = 'https://v3.football.api-sports.io/'
headers = {
    'x-apisports-key': 'd1097185ee42e79bae3f876df5733904',
    'content-type': 'application/json'
}

equipo_1 = input('Ingrese el nombre del equipo del jugador: ').title()

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

equipo_2 = input('Ingrese el nombre del equipo del jugador: ').title()

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
lista_jugadores = []

for i in range(2):
    jugador = input('Ingrese el nombre del jugador(apellido): ').title()
    if i != 0:
        tupla = (jugador, lista_equipos_2[0])
    else:
        tupla = (jugador, lista_equipos_1[0])
    lista_jugadores.append(tupla)

print(lista_jugadores)

for jugador, equipo in lista_jugadores:
    url_personalizada = f'https://v3.football.api-sports.io/players?search={jugador}&team={equipo}'
    contador = 0
    try:
        response_ = rq.get(url_personalizada, headers=headers)
        response_.raise_for_status()
        texto = response_.json()
        datos = json.dumps(texto, indent=4)
        if contador == 0:
            archivo_jugador_1 = texto
        else:
            archivo_jugador_2 = texto
        print(datos)
        contador += 1
    except rq.exceptions.HTTPError as e:
        print(f'Error HTTP: {e}')
    except rq.exceptions.RequestException as e:
        print(f'Error de conexion o solicitud: {e}')




### Mejora 4 ###

import asyncio
import aiohttp

url = 'https://v3.football.api-sports.io/'
headers = {
    'x-apisports-key': 'd1097185ee42e79bae3f876df5733904',
    'content-type': 'application/json'
}

async def encontrar_equipos(session, url_personalizada) -> list:
    try:
        async with session.get(url_personalizada, headers=headers) as respuesta:
            respuesta.raise_for_status()
            datos = await respuesta.json()
            lista_equipos_1 = [team['team']['id'] for team in datos['response']]
            return lista_equipos_1[:1]  # mantener solo el primer equipo
    except aiohttp.ClientResponseError as e:
        print(f'Error de HTTP: {e}')
    except aiohttp.ClientError as e:
        print(f'Error de conexión o de solicitud: {e}')

lista_equipos = []
lista_ids_equipos = []

async def main():
    for i in range(5):
        equipo = input('Ingrese un equipo: ')
        lista_equipos.append(equipo)

    async with aiohttp.ClientSession() as session:
        tareas = []
        for equipo in lista_equipos:
            url_equipo = f'https://v3.football.api-sports.io/teams?search={equipo}'
            tareas.append(encontrar_equipos(session, url_equipo))

        resultados = await asyncio.gather(*tareas)
        for i, ids in enumerate(resultados, start=1):
            print(f"ID del equipo {i}: {ids}")

        for ids in resultados:
            lista_ids_equipos.append(ids[0])  # Agrega solo el número dentro de cada sublista
        
        print(lista_ids_equipos)

# Ejecutar el bucle
asyncio.run(main())

async def encontrar_jugadores(session, url_jugador) -> list:
    try: 
        async with session.get(url_jugador, headers=headers) as respuesta:
            respuesta.raise_for_status()
            datos = await respuesta.json()
            lista_jugadores_1 = [player['player']['id'] for player in datos['response']]
            return lista_jugadores_1[:1]
    except aiohttp.ClientResponseError as e:
        print(f'Error de HTTP: {e}')
    except aiohttp.ClientError as e:
        print(f'Error de conexion o de solicitud: {e}')

lista_jugadores = []
lista_ids_jugadores = []

async def main2():
    for i in range(5):
        jugador = input(f'Ingrese el jugador del {lista_equipos[i]}: ')
        lista_jugadores.append(jugador)

    async with aiohttp.ClientSession() as session:
        tareas = []
        for num, jugador in enumerate(lista_jugadores):
            url_jugador = f'https://v3.football.api-sports.io/players?search={jugador}&team={lista_ids_equipos[num]}'
            tareas.append(encontrar_jugadores(session, url_jugador))

        resultados = await asyncio.gather(*tareas)
        for i, ids in enumerate(resultados, start=1):
            print(f'Id del jugador {i}: {ids}')

        for ids in resultados:
            lista_ids_jugadores.append(ids[0])

        print(lista_ids_jugadores)

asyncio.run(main2())

async def transferencias(session, url_transfers):
    try: 
        async with session.get(url_transfers, headers=headers) as respuesta:
            respuesta.raise_for_status()
            datos = await respuesta.json()
            lista_transferencias = []
            for equipos in datos['response'][0]['transfers']:
                equipo_entrada = equipos['teams']['in']['name']
                equipo_salida = equipos['teams']['out']['name']
                lista = [equipo_entrada, equipo_salida]
                lista_transferencias.extend(lista)
            return set(lista_transferencias)
    except aiohttp.ClientResponseError as e:
        print(f'Error de HTTP: {e}')
    except aiohttp.ClientError as e:
        print(f'Error de conexion o de solicitud: {e}')

async def main3():
    async with aiohttp.ClientSession() as session:
        tareas = []
        for id_jugador in lista_ids_jugadores:
            url_transfers = f'https://v3.football.api-sports.io/transfers?player={id_jugador}'
            tareas.append(transferencias(session, url_transfers))
        
        resultados = await asyncio.gather(*tareas)
        for equipos in resultados:
            print(f'El jugador ha jugado para: {equipos}')

asyncio.run(main3())

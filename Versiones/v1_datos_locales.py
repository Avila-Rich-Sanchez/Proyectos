# Bot

jugadores = {
    "Lionel Messi": ["Neymar Jr.", "Luis Suárez", "Andrés Iniesta", "Xavi Hernández", "Sergio Busquets", "Jordi Alba", "Kylian Mbappé", "Ángel Di María"],
    "Cristiano Ronaldo": ["Karim Benzema", "Gareth Bale", "Sergio Ramos", "Luka Modrić", "Marcelo", "Casemiro", "Bruno Fernandes", "Wayne Rooney"],
    "Robert Lewandowski": ["Thomas Müller", "Joshua Kimmich", "Manuel Neuer", "Serge Gnabry", "Arjen Robben", "Franck Ribéry", "Jamal Musiala", "Pedri"],
    "Kevin De Bruyne": ["Erling Haaland", "Phil Foden", "Bernardo Silva", "Rodri", "Jack Grealish", "Riyad Mahrez", "Vincent Kompany", "David Silva"],
    "Kylian Mbappé": ["Neymar Jr.", "Lionel Messi", "Achraf Hakimi", "Marco Verratti", "Ousmane Dembélé", "Warren Zaïre-Emery", "Presnel Kimpembe", "Gianluigi Donnarumma"],
    "Virgil van Dijk": ["Mohamed Salah", "Alisson Becker", "Trent Alexander-Arnold", "Fabinho", "Jordan Henderson", "Sadio Mané", "Andy Robertson", "Alexis Mac Allister"],
    "Vinicius Jr.": ["Jude Bellingham", "Rodrygo", "Federico Valverde", "Aurélien Tchouaméni", "Éder Militão", "Toni Kroos", "Luka Modrić", "Dani Carvajal"],
    "Erling Haaland": ["Kevin De Bruyne", "Phil Foden", "Julian Álvarez", "Bernardo Silva", "Rodri", "Manuel Akanji", "Jack Grealish", "Marco Reus"],
    "Neymar Jr": ["Lionel Messi", "Kylian Mbappé", "Luis Suárez", "Dani Alves", "Thiago Silva", "Marquinhos", "Marco Verratti", "Ronaldinho"],
    "Luka Modric": ["Toni Kroos", "Casemiro", "Karim Benzema", "Sergio Ramos", "Cristiano Ronaldo", "Vinicius Jr.", "Federico Valverde", "Dani Carvajal"]
}

def encontrar_jugador(jug_1, jug_2):
    
    compañeros_jug_1 = []
    if jug_1 in jugadores.keys():
        for i in jugadores[jug_1]:
            compañeros_jug_1.append(i)
    else:
        print('El jugador no esta en mi base de datos.')
        exit()

    compañeros_jug_2 = []
    if jug_2 in jugadores.keys():
        for i in jugadores[jug_2]:
            compañeros_jug_2.append(i)
    else:
        print('El jugador no esta en mi base de datos.')
        exit()

    compañeros_totales = compañeros_jug_1 + compañeros_jug_2
    compañeros_repetidos = []
    for i in compañeros_totales:
        if compañeros_totales.count(i) >= 2:
            compañeros_repetidos.append(i)

    compañeros_repetidos = set(compañeros_repetidos)
    if len(compañeros_repetidos) >= 2:
        print('Hay mas de un jugador.')
        print('Son:')
        print([jugador for jugador in compañeros_repetidos])
    elif len(compañeros_repetidos) == 1:
        print('El jugador es: ')
        print([jugador for jugador in compañeros_repetidos])
    elif not compañeros_repetidos:
        print('No hay compañeros en comun segun mi base de datos ;).')
        exit()

compañeros = []

while True:
    
    print('Que jugador jugo con: ')

    for i in range(2):
        jugador = input(f'Ingresa el nombre del jugador {i + 1}: ')
        compañeros.append(jugador.title())

    for num, name in enumerate(compañeros):
        print(f'{num + 1}. {name}')

    encontrar_jugador(compañeros[0], compañeros[1])
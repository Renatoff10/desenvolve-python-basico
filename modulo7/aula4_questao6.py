import csv

def processar_spotify():
    with open("spotify-2023.csv", "r", encoding='latin-1') as file:
        reader = csv.DictReader(file)
        musicas = list(reader)
    
    anos = range(2012, 2023)
    mais_tocadas = []

    for ano in anos:
        musicas_do_ano = [musica for musica in musicas if int(musica['released_year']) == ano]
        if musicas_do_ano:
            mais_tocada = max(musicas_do_ano, key=lambda x: int(x['streams']))
            mais_tocadas.append([
                mais_tocada['track_name'],
                mais_tocada['artist(s)_name'],
                mais_tocada['released_year'],
                mais_tocada['streams']
            ])
    
    print(mais_tocadas)

processar_spotify()

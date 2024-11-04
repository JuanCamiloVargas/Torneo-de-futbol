import json

def registrar_partido(fecha: str, equipo_local_id: str, equipo_visitante_id: str, goles_local: int, goles_visitante: int):
    with open("equipos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    equipo_local = None
    equipo_visitante = None

    for i in file["equipos"]:
        if i["id"] == equipo_local_id:
            equipo_local = i
    
        if i["id"] == equipo_visitante_id:
            equipo_visitante = i

    if (equipo_local == None or equipo_visitante == None):
        return "Uno de los equipos no existe"

    with open("partidos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    if file["partidos"]:
        lastId = int(file["partidos"][-1]["id"].replace("PAR", ""))
        currentId = lastId + 1
    else:
        currentId = 1

    partido = {
        "id": f"PAR{currentId}",  
        "fecha": fecha,  
        "id_arbitro": None,
        "equipo_local": equipo_local["id"],  
        "equipo_visitante": equipo_visitante["id"], 
        "goles_local": goles_local,  
        "goles_visitante": goles_visitante, 
        "alineacion_local": equipo_local["jugadores"],  
        "alineacion_visitante": equipo_visitante["jugadores"],
        "eventos": [  
            {
                "minuto": 30,
                "tipo": "gol",
                "jugador": "JUG001",
                "equipo": "EQP001"
            }
        ]
    }

    file["partidos"].append(partido)

    with open("partidos.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    return partido

def buscar_partido(criterio: str, valor: str) -> list:
    with open("partidos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    partidos = []

    for i in file["partidos"]:
        if (i[criterio] == valor):
            partidos.append(i)

    return partidos

# print(actualizar_estadisticas("EQP1", {"asdasdasd": 10}))

# print(buscar_partido("fecha", "2024-10-11"))
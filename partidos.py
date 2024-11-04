import json

def registrar_partido(fecha: str, equipo_local_id: str, equipo_visitante_id: str):
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

    for i in file["partidos"]:
        if i["fecha"] == fecha and i["equipo_local"] == equipo_local_id and i["equipo_visitante"] == equipo_visitante_id:
            return "El partido ya existe"

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
        "goles_local": 0,  
        "goles_visitante": 0, 
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

# print(registrar_partido("2024-10-11", "EQP1", "EQP2", 10, 2))

def actualizar_resultados(id: str, goles_local: int, goles_visitante: int):
    if goles_local < 0 or goles_visitante < 0:
        return "Los goles no pueden ser negativos"
    
    with open("partidos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["partidos"]:
        if i["id"] == id:
            partido = i

    partido["goles_local"] = goles_local
    partido["goles_visitante"] = goles_visitante

    with open("partidos.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    return "Partido actualizado correctamente"

# print(actualizar_resultados("PAR1", 10, 1))

def agregar_eventos(id: int, eventos: dict):
    with open("partidos.json", "r", encoding="utf-8") as archivo:
       file = json.load(archivo)

    for i in file["partidos"]:
        if i["id"] == id:
            partido = i
        else:
            return "El partido no existe"
        
    if partido["equipo_local"] != eventos["equipo"]:
        if partido["equipo_visitante"] != eventos["equipo"]:
            return "El equipo no existe en este partido"
        
    jugador = None

    for i in partido["alineacion_local"]:
        if i == eventos["jugador"]:
            jugador = i

    for i in partido["alineacion_visitante"]:
        if i == eventos["jugador"]:
            jugador = i

    if jugador == None:
        return "El jugador no existe en este partido"

    partido["eventos"].append(eventos)

    with open("partidos.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    return "Eventos agregados correctamente"

# print(agregar_eventos("PAR1", {
#                     "minuto": 10,
#                     "tipo": "Tarjeta roja",
#                     "jugador": "JUG1",
#                     "equipo": "EQP1"
#                 }))
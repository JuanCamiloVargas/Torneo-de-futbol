import json

def registrar_jugador(nombre: str, equipo_id: str, posicion: str, numero: str):
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    if file["jugadores"]:
        lastId = int(file["jugadores"][-1]["id"].replace("JUG", ""))
        currentId = lastId + 1
    else:
        currentId = 1

    jugador = jugador = {
        "id": f"JUG{currentId}",
        "nombre": nombre,  
        "numero": numero,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "estadisticas": {
            "partidos": 0,
            "goles": 0,
            "asistencias": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "minutos_jugados": 0
        }
    }
            
    file["jugadores"].append(jugador)

    with open("jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["jugadores"]:
        if i["id"] == equipo_id:
            i["jugadores"].append(jugador["id"])

    with open("jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)
        
    return file

# registrar_jugador("Migsasasuel", "EQP1","Defensa","4")

def buscar_jugador(criterio: str, valor: str) -> list:
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        jugadores = json.load(archivo)

    jugadores = []

    for i in jugadores["jugadores"]:
        if (i[criterio]== valor):
            jugadores.append(i)
                             
    
    return jugadores

def actualizar_estadisticas(id: str, estadisticas: dict):
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["jugadores"]:
        if i["id"] == id:
            equipo = i

    for clave in estadisticas:
        if (estadisticas[clave] < 0):
            return "Las estadísticas no pueden tener números negativos"
        else: 
            equipo["estadisticas"][clave] = estadisticas[clave]

    with open("jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, indent=4)

    return "Estadísticas actualizadas satisfactoriamente"

print(actualizar_estadisticas("JUG1", {"partidos": 10}))
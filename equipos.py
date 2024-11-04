import json

def registrar_equipo(nombre: str, ciudad: str, dt: str) -> dict:
    with open("equipos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["equipos"]:
            if i["nombre"] == nombre or i["dt"] == dt:
                return "El equipo ya existe"

    if file["equipos"]:
        lastId = int(file["equipos"][-1]["id"].replace("EQP", ""))
        currentId = lastId + 1
    else:
        currentId = 1

    equipo = {
        "id": f"EQP{currentId}",
        "nombre": nombre,
        "ciudad": ciudad,
        "dt": dt,
        "jugadores": [],
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "emapatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    }

    file["equipos"].append(equipo)

    with open("equipos.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    return equipo

def buscar_equipo(criterio: str, valor: str) -> list:
    with open("equipos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    equipos = []

    for i in file["equipos"]:
        if (i[criterio] == valor):
            equipos.append(i)

    return equipos

def actualizar_estadisticas(id: str, estadisticas: dict):
    with open("equipos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["equipos"]:
        if i["id"] == id:
            equipo = i

    for clave in estadisticas:
        if (estadisticas[clave] < 0):
            return "Las estadísticas no pueden tener números negativos"
        else: 
            equipo["estadisticas"][clave] = estadisticas[clave]

    with open("equipos.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, indent=4)

    return "Estadísticas actualizadas satisfactoriamente"


# print(actualizar_estadisticas("EQP1", {"asdasdasd": 10}))


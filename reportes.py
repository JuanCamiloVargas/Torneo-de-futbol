import json


def generar_tabla_posiciones() -> list:
  
    with open("equipos.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)
    
    tabla_posiciones = sorted(
        file["equipos"],
        key=lambda equipo: equipo["estadisticas"]["puntos"],
        reverse=True
    )
    
    return tabla_posiciones

def generar_lista_goleadores(top: int = 10) -> list:
  
    goleadores = []
    
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)
    
   
    for jugador in file["jugadores"]:
        goleadores.append({
            "nombre": jugador["nombre"],
            "equipo_id": jugador["equipo_id"],
            "goles": jugador["estadisticas"]["goles"]
        })
    
    
    goleadores_top = sorted(
        goleadores, 
        key=lambda jugador: jugador["goles"],
        reverse=True)[:top]
    
    return goleadores_top

def generar_estadisticas_equipo(id_equipo: str) -> dict:
   
    with open("equipos.json", "r", encoding="utf-8") as archivo_equipos:
        equipos_file = json.load(archivo_equipos)
    
    with open("jugadores.json", "r", encoding="utf-8") as archivo_jugadores:
        jugadores_file = json.load(archivo_jugadores)

    equipo = None

    for i in equipos_file["equipos"]:
        if i["id"] == id_equipo:
            equipo = i

    if equipo == None:
        return "El equipo no existe"

    jugadores_equipo = [
        jugador for jugador in jugadores_file["jugadores"] if jugador["equipo_id"] == id_equipo
    ]
    
    puntos_obtenidos = equipo["estadisticas"]["puntos"]
    puntos_disponibles = equipo["estadisticas"]["partidos_jugados"] * 3
    rendimiento = (puntos_obtenidos / puntos_disponibles) if puntos_disponibles > 0 else 0
    
    
    estadisticas_equipo = {
        "nombre": equipo["nombre"],
        "ciudad": equipo["ciudad"],
        "dt": equipo["dt"],
        "estadisticas": equipo["estadisticas"],
        "rendimiento": round(rendimiento, 2),
        "jugadores": jugadores_equipo
    }
    
    return estadisticas_equipo

import json

def generar_reporte_completo():
   
    
    tabla_posiciones = generar_tabla_posiciones()
    lista_goleadores = generar_lista_goleadores(top=10)
    
    
    estadisticas_equipos = []
    for equipo in tabla_posiciones:
        id_equipo = equipo["id"]
        estadisticas_equipo = generar_estadisticas_equipo(id_equipo)
        estadisticas_equipos.append(estadisticas_equipo)
    
    
    reportes = {
        "tabla_posiciones": tabla_posiciones,
        "goleadores": lista_goleadores,
        "estadisticas_equipos": estadisticas_equipos
    }
    
    
    with open("reportes.json", "w", encoding="utf-8") as archivo:
        json.dump(reportes, archivo, ensure_ascii=False, indent=4)
    
    return "Reporte completo generado en 'reportes.json'"


print(generar_reporte_completo())

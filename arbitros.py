import json
from textwrap import indent

def registrar_arbitro(nombre: str, experiencia: int, categoria: str):
    categorias = ["FIFA", "Nacional", "Regional"]

    flag = False

    for i in categorias:
        if i == categoria:
            flag = True

    if flag == False:
        return "La categoría debe ser igual a uno de los siguientes valores: FIFA, Nacional o Regional"

    with open("arbitros.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    for i in file["arbitros"]:
        if i["nombre"] == nombre:
            return "El arbitro ya fue registrado"

    if file["arbitros"]:
        lastId = int(file["arbitros"][-1]["id"].replace("ARB", ""))
        currentId = lastId + 1
    else:
        currentId = 1

    arbitro = {
                "id": f"ARB{currentId}",
                "nombre": nombre,
                "experiencia": experiencia,
                "categoria": categoria,
                "partidos_dirigidos": 0
              }
    
    file["arbitros"].append(arbitro)

    with open("arbitros.json", "w", encoding="utf-8") as archivo:
        json.dump(file, archivo, ensure_ascii=False, indent=4)

    return arbitro

# print(registrar_arbitro("Carlos", 5, "FIFA"))

def asignar_arbitro(id_partido: str, id_arbitro: str):
    with open("arbitros.json", "r", encoding="utf-8") as archivo:
        fileArb = json.load(archivo)

    arbitro = None

    for i in fileArb["arbitros"]:
        if i["id"] == id_arbitro:
            arbitro = i

    if arbitro == None:
        return "El arbitro no existe"
    
    with open("partidos.json", "r", encoding="utf-8") as archivo:
        filePar = json.load(archivo)

    partido = None

    for i in filePar["partidos"]:
        if i["id"] == id_partido:
            partido = i
    
    if partido == None:
        return "El partido no existe"
    
    partido["id_arbitro"] = arbitro["id"]

    arbitro["partidos_dirigidos"] += 1

    with open("partidos.json", "w", encoding="utf-8") as archivo:
        json.dump(filePar, archivo, ensure_ascii=False, indent=4)

    with open("arbitros.json", "w", encoding="utf-8") as archivo:
        json.dump(fileArb, archivo, ensure_ascii=False, indent=4)

    return "Arbitro asignado correctamente"

# print(asignar_arbitro("PAR1", "ARB1"))

def generar_reporte_arbitros():
    with open("arbitros.json", "r", encoding="utf-8") as archivo:
        file = json.load(archivo)

    file["arbitros"].sort(key=lambda i: i["partidos_dirigidos"], reverse=True)

    for i in file["arbitros"]:
        print(f"\n{i}")

    return file["arbitros"]

generar_reporte_arbitros()
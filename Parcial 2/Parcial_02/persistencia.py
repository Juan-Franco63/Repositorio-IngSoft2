import json
from tareas.tarea_normal import TareaNormal
from tareas.tarea_importante import TareaImportante

ARCHIVO = "tareas.json"

def guardar_tareas(tareas):
    data = []
    for t in tareas:
        tipo = "normal" if isinstance(t, TareaNormal) else "importante"
        data.append({
            "descripcion": t.descripcion,
            "completada": t.completada,
            "tipo": tipo
        })
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

def cargar_tareas():
    try:
        with open(ARCHIVO, "r") as f:
            data = json.load(f)
            tareas = []
            for t in data:
                if t["tipo"] == "normal":
                    tarea = TareaNormal(t["descripcion"])
                else:
                    tarea = TareaImportante(t["descripcion"])
                if t["completada"]:
                    tarea.completar()
                tareas.append(tarea)
            return tareas
    except FileNotFoundError:
        return []

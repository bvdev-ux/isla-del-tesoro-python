"""Guarda las cinco mejores puntuaciones en un archivo local."""

import json
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent.parent / "records.json"


def guardar(puntos, archivo=ARCHIVO):
    try:
        datos = json.loads(archivo.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        datos = []
    if not isinstance(datos, list):
        datos = []
    datos = [n for n in datos if type(n) is int and n >= 0]
    mejores = sorted([*datos, puntos], reverse=True)[:5]
    archivo.write_text(json.dumps(mejores, indent=2) + "\n", encoding="utf-8")
    return mejores

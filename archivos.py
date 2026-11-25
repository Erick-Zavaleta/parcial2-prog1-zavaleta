
import json

RUTA_ARCHIVO = "alumnos.json"


def cargar_alumnos(ruta=RUTA_ARCHIVO):
    archivo_creacion = open(ruta, "a", encoding="utf-8")
    archivo_creacion.close()

    archivo_lectura = open(ruta, "r", encoding="utf-8")
    contenido = archivo_lectura.read()
    archivo_lectura.close()

    if len(contenido) == 0:
        return []

    datos = json.loads(contenido)
    return datos


def guardar_alumnos(lista_alumnos, ruta=RUTA_ARCHIVO):
    archivo = open(ruta, "w", encoding="utf-8")
    contenido_json = json.dumps(lista_alumnos, indent=4)
    archivo.write(contenido_json)
    archivo.close()
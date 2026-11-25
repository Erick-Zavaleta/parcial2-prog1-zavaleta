
def cantidad_total_alumnos(lista_alumnos):
    return len(lista_alumnos)


def calcular_promedio_notas(lista_alumnos):
    total = len(lista_alumnos)
    if total == 0:
        return 0.0

    acumulador = 0.0
    for i in range(total):
        acumulador = acumulador + lista_alumnos[i]["nota"]

    return acumulador / total


def obtener_alumnos_mayor_nota(lista_alumnos):
    if len(lista_alumnos) == 0:
        return []

    mayor_nota = lista_alumnos[0]["nota"]
    for i in range(1, len(lista_alumnos)):
        if lista_alumnos[i]["nota"] > mayor_nota:
            mayor_nota = lista_alumnos[i]["nota"]

    mejores = []
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["nota"] == mayor_nota:
            mejores = mejores + [lista_alumnos[i]]

    return mejores


def contar_aprobados(lista_alumnos):
    aprobados = 0
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["nota"] >= 6.0:
            aprobados = aprobados + 1
    return aprobados


def contar_desaprobados(lista_alumnos):
    desaprobados = 0
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["nota"] < 6.0:
            desaprobados = desaprobados + 1
    return desaprobados


def mostrar_estadisticas(lista_alumnos):
    print("\n--- ESTADISTICAS ---")
    total = cantidad_total_alumnos(lista_alumnos)
    print("Cantidad total de alumnos:", total)

    if total == 0:
        print("No hay datos suficientes para calcular promedio ni mayor nota.")
        return

    promedio = calcular_promedio_notas(lista_alumnos)
    aprobados = contar_aprobados(lista_alumnos)
    desaprobados = contar_desaprobados(lista_alumnos)
    mejores = obtener_alumnos_mayor_nota(lista_alumnos)

    print("Promedio de notas:", promedio)
    print("Cantidad de aprobados (>= 6):", aprobados)
    print("Cantidad de desaprobados (< 6):", desaprobados)
    print("Alumno(s) con mayor nota (nota:", mejores[0]["nota"], "):")
    for i in range(len(mejores)):
        print(" -", mejores[i]["nombre"], mejores[i]["apellido"], "(DNI:", mejores[i]["dni"], ")")
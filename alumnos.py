
from validaciones import (
    leer_entero,
    leer_flotante,
    leer_texto_no_vacio,
    dni_existe,
    edad_valida,
    nota_valida,
)
from archivos import guardar_alumnos


def crear_diccionario_alumno(dni, nombre, apellido, edad, nota):
    return {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota,
    }


def mostrar_un_alumno(alumno):
    print("DNI:", alumno["dni"])
    print("Nombre:", alumno["nombre"])
    print("Apellido:", alumno["apellido"])
    print("Edad:", alumno["edad"])
    print("Nota:", alumno["nota"])
    print("-" * 25)


def registrar_alumno(lista_alumnos):
    print("\n--- REGISTRAR ALUMNO ---")
    dni = leer_entero("Ingrese DNI: ")
    if dni_existe(lista_alumnos, dni):
        print("Error: ya existe un alumno registrado con ese DNI.")
        return lista_alumnos

    nombre = leer_texto_no_vacio("Ingrese Nombre: ")
    apellido = leer_texto_no_vacio("Ingrese Apellido: ")

    edad = leer_entero("Ingrese Edad: ")
    while not edad_valida(edad):
        print("Error: la edad no puede ser negativa.")
        edad = leer_entero("Ingrese Edad nuevamente: ")

    nota = leer_flotante("Ingrese Nota final (0 a 10): ")
    while not nota_valida(nota):
        print("Error: la nota debe estar entre 0 y 10.")
        nota = leer_flotante("Ingrese Nota final nuevamente (0 a 10): ")

    nuevo_alumno = crear_diccionario_alumno(dni, nombre, apellido, edad, nota)
    lista_alumnos = lista_alumnos + [nuevo_alumno]
    guardar_alumnos(lista_alumnos)
    print("Alumno registrado y guardado correctamente.")
    return lista_alumnos


def listar_alumnos(lista_alumnos):
    print("\n--- LISTADO DE ALUMNOS ---")
    if len(lista_alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    for i in range(len(lista_alumnos)):
        mostrar_un_alumno(lista_alumnos[i])


def buscar_indice_alumno(lista_alumnos, dni):
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["dni"] == dni:
            return i
    return -1


def buscar_alumno(lista_alumnos):
    print("\n--- BUSCAR ALUMNO ---")
    if len(lista_alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    dni = leer_entero("Ingrese DNI a buscar: ")
    indice = buscar_indice_alumno(lista_alumnos, dni)
    if indice != -1:
        mostrar_un_alumno(lista_alumnos[indice])
    else:
        print("No se encontro ningun alumno con el DNI ingresado.")


def modificar_alumno(lista_alumnos):
    print("\n--- MODIFICAR ALUMNO ---")
    if len(lista_alumnos) == 0:
        print("No hay alumnos registrados.")
        return lista_alumnos

    dni = leer_entero("Ingrese DNI del alumno a modificar: ")
    indice = buscar_indice_alumno(lista_alumnos, dni)
    if indice == -1:
        print("No se encontro ningun alumno con ese DNI.")
        return lista_alumnos

    alumno_actual = lista_alumnos[indice]
    mostrar_un_alumno(alumno_actual)

    print("Que campo desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Nota")
    opcion = leer_entero("Seleccione una opcion (1-4): ")

    if opcion == 1:
        alumno_actual["nombre"] = leer_texto_no_vacio("Nuevo Nombre: ")
    elif opcion == 2:
        alumno_actual["apellido"] = leer_texto_no_vacio("Nuevo Apellido: ")
    elif opcion == 3:
        nueva_edad = leer_entero("Nueva Edad: ")
        while not edad_valida(nueva_edad):
            print("Error: la edad no puede ser negativa.")
            nueva_edad = leer_entero("Nueva Edad nuevamente: ")
        alumno_actual["edad"] = nueva_edad
    elif opcion == 4:
        nueva_nota = leer_flotante("Nueva Nota (0 a 10): ")
        while not nota_valida(nueva_nota):
            print("Error: la nota debe estar entre 0 y 10.")
            nueva_nota = leer_flotante("Nueva Nota nuevamente (0 a 10): ")
        alumno_actual["nota"] = nueva_nota
    else:
        print("Opcion invalida.")
        return lista_alumnos

    lista_alumnos[indice] = alumno_actual
    guardar_alumnos(lista_alumnos)
    print("Alumno modificado y guardado correctamente.")
    return lista_alumnos


def eliminar_alumno(lista_alumnos):
    print("\n--- ELIMINAR ALUMNO ---")
    if len(lista_alumnos) == 0:
        print("No hay alumnos registrados.")
        return lista_alumnos

    dni = leer_entero("Ingrese DNI del alumno a eliminar: ")
    indice = buscar_indice_alumno(lista_alumnos, dni)
    if indice == -1:
        print("No se encontro ningun alumno con ese DNI.")
        return lista_alumnos

    nueva_lista = []
    for i in range(len(lista_alumnos)):
        if i != indice:
            nueva_lista = nueva_lista + [lista_alumnos[i]]

    guardar_alumnos(nueva_lista)
    print("Alumno eliminado y cambios guardados.")
    return nueva_lista
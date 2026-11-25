
from archivos import cargar_alumnos
from alumnos import (
    registrar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_alumno,
    eliminar_alumno,
)
from estadisticas import mostrar_estadisticas
from validaciones import leer_entero


def mostrar_menu():
    print("\n========== GESTION DE ALUMNOS ==========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadisticas")
    print("7. Salir")


def ejecutar_sistema():
    alumnos = cargar_alumnos()
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opcion: ")

        if opcion == 1:
            alumnos = registrar_alumno(alumnos)
        elif opcion == 2:
            listar_alumnos(alumnos)
        elif opcion == 3:
            buscar_alumno(alumnos)
        elif opcion == 4:
            alumnos = modificar_alumno(alumnos)
        elif opcion == 5:
            alumnos = eliminar_alumno(alumnos)
        elif opcion == 6:
            mostrar_estadisticas(alumnos)
        elif opcion == 7:
            print("Saliendo del sistema...")
            continuar = False
        else:
            print("Opcion no valida. Intente nuevamente.")


ejecutar_sistema()
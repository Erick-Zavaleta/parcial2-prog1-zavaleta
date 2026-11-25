
def es_caracter_digito(caracter):
    return caracter >= "0" and caracter <= "9"


def es_entero_valido(texto):
    if len(texto) == 0:
        return False

    inicio = 0
    if texto[0] == "-":
        if len(texto) == 1:
            return False
        inicio = 1

    for i in range(inicio, len(texto)):
        if not es_caracter_digito(texto[i]):
            return False

    return True


def es_numero_valido(texto):
    if len(texto) == 0:
        return False

    puntos = 0
    digitos = 0
    for i in range(len(texto)):
        if es_caracter_digito(texto[i]):
            digitos = digitos + 1
        elif texto[i] == ".":
            puntos = puntos + 1
            if puntos > 1:
                return False
        else:
            return False

    return digitos > 0


def leer_entero(mensaje):
    valido = False
    valor_entero = 0
    while not valido:
        entrada = input(mensaje)
        if es_entero_valido(entrada):
            valor_entero = int(entrada)
            valido = True
        else:
            print("Error: ingrese un numero entero valido.")
    return valor_entero


def leer_flotante(mensaje):
    valido = False
    valor_flotante = 0.0
    while not valido:
        entrada = input(mensaje)
        if es_numero_valido(entrada):
            valor_flotante = float(entrada)
            valido = True
        else:
            print("Error: ingrese un numero valido (use punto si tiene decimales).")
    return valor_flotante


def leer_texto_no_vacio(mensaje):
    valido = False
    texto = ""
    while not valido:
        texto = input(mensaje)
        tiene_contenido = False
        for i in range(len(texto)):
            if texto[i] != " ":
                tiene_contenido = True
        if tiene_contenido:
            valido = True
        else:
            print("Error: el campo no puede estar vacio.")
    return texto


def dni_existe(lista_alumnos, dni):
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["dni"] == dni:
            return True
    return False


def edad_valida(edad):
    return edad >= 0 and edad <= 120


def nota_valida(nota):
    return nota >= 0.0 and nota <= 10.0
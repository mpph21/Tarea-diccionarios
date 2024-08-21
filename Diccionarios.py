def imprimir_valores_ascendentes(diccionario):
    valores = list(diccionario.values())
    valores.sort()
    print(valores)

# Ejemplo de uso
mi_diccionario = {"a": 3, "b": 1, "c": 2}
imprimir_valores_ascendentes(mi_diccionario)

def verificar_claves(diccionario1, diccionario2):
    for clave in diccionario1.keys():
        if clave not in diccionario2:
            return False
    return True

# Ejemplo de uso
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"a": 10, "b": 20, "c": 30}
print(verificar_claves(diccionario1, diccionario2))

def mezclar_diccionarios(diccionario1, diccionario2):
    nuevo_diccionario = diccionario2.copy()
    nuevo_diccionario.update(diccionario1)
    return nuevo_diccionario

# Ejemplo de uso
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4}
print(mezclar_diccionarios(diccionario1, diccionario2))


def imprimir_personas_mayores(personas):
    for persona in personas:
        if persona["edad"] > 100:
            print(persona["nombres"])

# Ejemplo de uso
personas = [
    {"nombres": "Pedro Julio", "apellidos": "Castro", "edad": 101},
    {"nombres": "Juan Carlos", "apellidos": "Pérez", "edad": 50},
    {"nombres": "Ana María", "apellidos": "García", "edad": 102}
]
imprimir_personas_mayores(personas)


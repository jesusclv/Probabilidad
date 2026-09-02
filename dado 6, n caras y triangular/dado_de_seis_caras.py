##
#! Script que cuenta el número de eventos de un dado virtual de 6 caras.
import random

lanzamientos = 10000

#? Diccionario para contar los lanzamientos por cara.
resultados = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

#? Realizamos los lanzamientos.
for _ in range(lanzamientos):
    cara = random.randint(1, 6)
    resultados[cara] += 1

print(f'\nLos lanzamientos para este caso son: {lanzamientos}\n')

#? Mostramos los resultados.
for cara, conteo in resultados.items():
    print(f'Cara {cara}: {conteo} veces')

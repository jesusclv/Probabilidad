##
#! Script que cuenta el número de eventos de un dado virtual de 'n' caras.
import random

#? Solicitamos al usuario que ingrese el número de caras y definimos los lanzamientos.
n_caras = int(input('\nIngresa el número de caras del dado: '))
lanzamientos = 10000

#? Diccionario para contar los lanzamientos por cara.
resultados = {
    i: 0 for i in range(1, n_caras + 1)
}

#? Realizamos los lanzamientos.
for _ in range(lanzamientos):
    cara = random.randint(1, n_caras)
    resultados[cara] += 1

#? Mostramos información relevante.
print(f'\nLos lanzamientos para este caso son: {lanzamientos}\n')
print(f'\nDado utilizado: {n_caras} caras\n')

#? Mostramos los resultados.
for cara, conteo in resultados.items():
    print(f'Cara {cara}: {conteo} veces')

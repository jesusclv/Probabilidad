##
##! Script que crea un triángulo con 10000 puntos.
import random
import matplotlib.pyplot as plt

#? Definimos las coordenadas (X, Y) de los tres vértices del triángulo equilátero
vertices_x = [0.0, 1.0, 0.5]
vertices_y = [0.0, 0.0, 0.866]

#? Generamos el primer punto inicial en una ubicación completamente aleatoria
punto_x = random.uniform(0, 1)
punto_y = random.uniform(0, 1)

#? Listas para almacenar todos los puntos trazados y graficarlos al final
puntos_x = [punto_x]
puntos_y = [punto_y]

#? Definimos los 10,000 lanzamientos del dado
lanzamientos = 10000

#? Ciclo iterativo para calcular los puntos medios
for _ in range(lanzamientos):
    #* Lanzamos el dado de 3 caras (usamos índices 0, 1 y 2 para mapear a los vértices)
    dado = random.randint(0, 2)
    
    #* Calculamos la mitad exacta de la distancia hacia el vértice seleccionado
    punto_x = (punto_x + vertices_x[dado]) / 2
    punto_y = (punto_y + vertices_y[dado]) / 2
    
    #* Registramos la nueva posición
    puntos_x.append(punto_x)
    puntos_y.append(punto_y)

#? Visualización directa sin animaciones paso a paso
print("Calculando coordenadas y generando el gráfico...")
plt.figure(figsize=(8, 8))
plt.scatter(puntos_x, puntos_y, s=0.2, color='blue') #* s=0.2 define el tamaño pequeño del punto
plt.scatter(vertices_x, vertices_y, color='red', marker='^', s=50) #* Marcamos los 3 vértices en rojo
plt.title("Fase 3: 10,000 Puntos Generados")
plt.axis('off')
plt.show()
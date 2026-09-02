# Probabilidad - Dados

## Descripción del Proyecto
Este repositorio contiene la tarea uno tarea de probabilidad, La cual consta de 3 fases principales.

## Fases del Proyecto

### Fase 1: Simulación de Dado Estándar de 6 Caras
- Se elabora un script que simula el lanzamiento de un dado de 6 caras iterado 10,000 veces.
- El programa almacena en un diccionario la frecuencia de ocurrencia de cada evento (del 1 al 6) y muestra los resultados finales en consola.

### Fase 2: Simulación de Dado de múltiples caras ($n$ Caras)
- El script solicita al usuario ingresar el número de caras deseadas para el dado virtual (por ejemplo, 10, 100, o 500 caras).
- El diccionario de resultados se genera automáticamente según el número de caras ingresado.
- Tras simular los 10,000 lanzamientos, se imprime el registro de las frecuencias al igual que en la fase 1.

### Fase 3: Geometría y Probabilidad (El Juego del Caos)
1. **El Tablero**: Se define un triángulo equilátero mediante tres vértices fijos (1, 2 y 3) en la pantalla.
2. **El Inicio**: Se genera un punto inicial completamente aleatorio en el plano.
3. **El Dado Virtual**: Se utiliza un dado de 3 caras, donde cada resultado se vincula a uno de los 3 vértices.
4. **El Ciclo Iterativo**: Durante 10,000 iteraciones, se lanza el dado. El algoritmo mide la distancia desde el punto actual hasta el vértice correspondiente al lanzamiento, calcula el punto medio exacto y traza ahí una nueva coordenada.
5. **Renderizado**: Todos los puntos calculados se almacenan y se dibujan de forma simultánea al finalizar utilizando la librería `matplotlib`.

## Instalación y Requisitos
Las primeras dos fases utilizan únicamente la librería estándar `random` de Python. Para visualizar la Fase 3, es necesario instalar `matplotlib`:

```bash
pip install matplotlib

# Reto German emotional audio
## Descripcion
El [Berlin emotional Dataset](http://emodb.bilderbar.info/index-1024.html) es un conjunto de audios de actores alemanes que pronuncias frases con distintas emociones

Este dataset contiene alrededror de 500 audios en siete diferentes emociones. 
El reto es construir un clasificador de que sea capaz de reconocer las emociones presentes en el audio.
Hay tres problemas que se pueden resolver.

1: Emociones de alta vs. baja excitación (rabia vs. tristeza, entre otros)
2: Emociones positivas vs. negativas (alegria vs. tristeza, entre otros)
3: Clasificación de las siete emociones.



### Variables

Se proveen algunas características calculadas sobre los audios (144), que corresponden a un arreglo de [Coeficientes cepstrales en frecuencias de Mel](https://es.wikipedia.org/wiki/MFCC)

El archivo `Features.txt` contiene 144 características calculadas para cada audio, formando una matriz de `535x144` usando la función incluida en `extract_features.py`.



### Objetivo
1. Crear un algoritmo que tome un audio de entrada, calcule las características, y retorne la clase (`class_id`) a la que pertence el audio.
1. Entrenar este algoritmo utilizando los datos de entrenamiento`.
1. Medir el desempeño del algoritmo utilizando los datos de test. El desempeño debe ser medido como
```python
score = n_aciertos / n_audios * 100
```
donde `n_aciertos` es el numero de audios clasificados de forma correcta y `n_audios` es el numero total de audios en el conjunto de test.

### Notas Teoricas
* Esta es una base de datos pequeña, se recomienda el uso de técnicas clasicas de machine learning como arboles de decision o maquinas de soprte vectorial.

### Ejemplo y baseline
Ver procedimiento de [solucion](https://github.com/jcvasquezc/colomb-ia-supervised-emoDB/emoDB.ipynb).

##### Requerimientos
*Indica los requerimientos para utilizar el codigo de tu solucion.*

##### Procedimiento
*Indica el procedimiento que se debe seguir para reproducir tu solucion.*

##### Metodo
*Indica el metodo que utilizaste para solucionar el reto.*

##### Resultados
*Indica el metodo que utilizaste para solucionar el reto.*

## Getting Started
Para resolver este reto primero has un [fork](https://help.github.com/articles/fork-a-repo/) de este repositorio y [clona](https://help.github.com/articles/cloning-a-repository/) el fork en tu maquina.

```bash
git clone https://github.com/{username}/colomb-ia-emoDB
cd colomb-ia-emoDB
```

*Nota: reemplaza `{username}` con tu nombre de usuario de Github.*

### Requerimientos

* numpy
* jupyter
* scipy

# Starter Code Python
Para iniciar con este reto puedes correr el codigo de Python en Jupyter del archivo `emoDB.ipynb`. Este código que ayudará a cargar y visualizar algunas imágenes. Las dependencias son las mismas que se instalaron durante la descarga de los datos, ver [Requerimientos](#requerimientos).

Para iniciar el código solo hay que prender Jupyter en esta carpeta

```bash
jupyter notebook .
```
y abrir el archivo `emoDB.ipynb`.

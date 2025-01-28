# Prácticas de la librería Numpy.
- ### Importamos Numpy con su abreviación "np".
```
import numpy as np
```

- ### Podemos crear arrays de una dimensión con la función np.array()
```
array_unidim = np.array([1,2,3,4,5])
```

- ### O un array de dos dimensiones (bidimensional)
```
array_bidim = np.array([[1,2,3],[4,5,6]])
```

-### O un array de tres dimensiones (tridimensional)
```
array_tridim = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
```

## Para cada uno de estos arrays, podemos obtener sus propiedades, tales como su "forma", número de dimensiones, tipos de datos y tamaño.
- ### Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
```
array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim)
```
![image](https://github.com/user-attachments/assets/201b524d-6134-4643-805d-d9ada619f42e)

- ### Atributos del array bidimensional
```
array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim)
```
![image](https://github.com/user-attachments/assets/7290890e-cef2-47c9-a00d-1c6bb16f3727)

- ### Atributos del array tridimensional
```
array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim)
```
![image](https://github.com/user-attachments/assets/2d23b7d7-c6aa-41ca-b9af-2acf64e44491)

- ### Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional.
```
import pandas as pd

datos = pd.DataFrame(array_bidim)
datos
```
![image](https://github.com/user-attachments/assets/55b2761b-e463-4a48-be5d-4e70ea710876)

- ### # Creamos un array de tamaño 4x3, formado únicamente por unos (1)
```
unos = np.ones((4,3))
unos
```
![image](https://github.com/user-attachments/assets/63bf2a55-9d71-4185-829e-1ba5828ec167)

- ### Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
```
ceros = np.zeros((2,4,3))
ceros
```
![image](https://github.com/user-attachments/assets/f40f58a6-a3b2-4529-aed3-3a59a4f2877e)

- ### Creamos un array de números en el rango de 0 a 100, con un paso de 5.
```
array1 = np.arange(0,100,5)
array1
```
![image](https://github.com/user-attachments/assets/d54d77e8-8acf-43f3-bb0b-12f6cda6f0d7)

- ### Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5).
```
array2 = np.random.randint(0,10,(2,5))
array2
```
![image](https://github.com/user-attachments/assets/454a3d58-6372-4948-81eb-b1f515885bcc)

- ### Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5).
```
array3 = np.random.random((3,5))
array3
```
![image](https://github.com/user-attachments/assets/af536b6a-d2a6-4e18-8375-1c016a96209e)

- ### Establecemos la "semilla" de números aleatorios en 27.
```
np.random.seed(27)
```

- ### Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5).
```
array4 = np.random.randint(0,10,(3,5))
array4
```
![image](https://github.com/user-attachments/assets/ea02d87c-fe72-4ff4-8f40-0c56023cdfb2)

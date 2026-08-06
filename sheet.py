# 📌 Cheat Sheet - Todo lo aprendido

## 📚 Librerías

### C
```c
#include <stdio.h>
#include <time.h>
```

### Python
```python
import time
import numpy as np
```

## 🧮 Matrices

### C
```c
int matriz[3][3] = {
    {1,2,3},
    {4,5,6},
    {7,8,9}
};
```

### Python
```python
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

## 🔄 Multiplicación de matrices (Python)

```python
for i in range(3):
    for j in range(3):
        for k in range(3):
            resultado[i][j] += A[i][k] * B[k][j]
```

## 📊 NumPy

:contentReference[oaicite:1]{index=1}

```python
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

C = np.dot(A, B)
# o
C = A @ B
```

## ⏱️ Medición de tiempo

### C
```c
#include <time.h>

clock_t inicio = clock();

/* código */

clock_t fin = clock();

double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
```

### Python
```python
import time

inicio = time.time()

# código

fin = time.time()

print(fin - inicio)
```

## 🧑‍💻 Git / GitHub

:contentReference[oaicite:2]{index=2} + :contentReference[oaicite:3]{index=3}

```bash
git init
git add .
git commit -m "mensaje"
git push
```

```bash
git status
git log --oneline
```

## 🎯 Resumen

- Librerías en C y Python  
- Matrices 3x3  
- Multiplicación de matrices  
- NumPy  
- Medición de tiempo  
- Git y GitHub  
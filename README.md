# Reto-7

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
n = 0
cuadrado = n ** 2
while n <= 100:
  print("Numero " + str(n) + " , Cuadrado = " + str(cuadrado) +  " ") 
  n = n + 1
  cuadrado = n ** 2
  ```


### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000


```python
n = 1
print("Números impares:")
while n <= 999:
  print(n)
  n += 2
n2 = 2
print("Números pares:")
while True:
  print(n2)
  n2 += 2
  if n2 > 1000:
    break
```


### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
def pares_des(n):
  if n < 2:
    print("El numero debe ser mayor o igual a 2")
    return
  print("Numeros pares descendentes hasta 2")
  while n >= 2:
    if n % 2 == 0:
      print(n)
      n -= 2
n = int(input("Escriba un numero natural mayor o igual a 2"))
pares_des(n)
```


### 4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

``` python
pais_a = 25e6
pais_b = 18.9e6
tasa_c_a = 0.02
tasa_c_b = 0.03
ano = 2022
while pais_b <= pais_a:
    pais_a *= (1 + tasa_c_a)
    pais_b *= (1 + tasa_c_b)
    ano += 1
print("La poblacion del pais B sobrepasara a la del pais A en el ano:", ano)
print("Población del pais A: " + str(pais_a) + " habitantes")
print("Población del pais B: " + str(pais_b) + " habitantes")
```


### 5. Imprimir el factorial de un número natural n dado.

``` python
n = int(input("Escriba un numero natural para calcular el factorial"))
if n >= 0:
    fact = 1
    cont = n
    while cont > 0:
        fact *= cont
        cont -= 1
    print("El factorial de " + str(n) + " es: " + str(fact) + "")
else:
    print("Los numero negativos no tienen factorial, escribrir un entero positivo")
```


### 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

``` python
import random
n_secreto = random.randint(1, 100)
veces = 0
while True:
  veces += 1
  adivina = int(input("Introduce un número del 1 al 100: "))
  if adivina == n_secreto:
    print("¡Felicidades! adivinaste el numero en " + str(veces) + " intentos")
    break
  elif adivina < n_secreto:
    print("El numero secreto es mayor del que tu piensas")
  else:
    print("El numero secreto es menor del que tu piensas")
```


### 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

``` python
n = int(input("Escriba un numero entre 2 y 50"))
if 2 <= n <= 50:
    print("Los divisores de " + str(n) + " son:")
    div = 1
    while div <= n:
        if n % div == 0:
            print(div)
        div += 1
else:
    print("El numero escrito no esta dentro del rango")
```


### 8. Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

``` python
def primos(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
def most_primos():
    n = 1
    print("Numeros primos del 1 al 100")
    while n <= 100:
        if primos(n):
            print(n, end=" ")
        n += 1
most_primos()
```

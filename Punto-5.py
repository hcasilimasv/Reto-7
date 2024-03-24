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
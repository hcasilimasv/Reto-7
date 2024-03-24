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
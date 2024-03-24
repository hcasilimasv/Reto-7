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
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
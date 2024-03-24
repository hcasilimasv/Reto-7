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
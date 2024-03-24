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
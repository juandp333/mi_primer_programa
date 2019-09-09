#Transformanr de grados Farenheit a centigrados ( Celsius = Farenheit -32/1.8) Mstar en formaeteado con .format

grado_inicial = int(input("Cuantos grado Farenhet tienes:"))

resltado = (grado_inicial - 32) /1.8
print(str("la conversion es {} Celsius".format(resltado)))
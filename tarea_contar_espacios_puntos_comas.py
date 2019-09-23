#Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario

texto_usuario = input("Hola por favor ingresa tu texto a contar: (ESPACIOS, PUNTOS y COMAS): ").upper()

signo_punto = ["."]
signo_coma = [","]
signo_espacio = [" "]

n_signos_punto = 0
n_signo_coma = 0
n_signo_espacio = 0

for letra in texto_usuario:
    if letra in signo_punto:
        n_signos_punto += 1
    elif letra in signo_coma:
        n_signo_coma += 1
    elif letra in signo_espacio:
        n_signo_espacio += 1

print("Los puntos son {}" .format(n_signos_punto))
print("Las comas son {}" .format(n_signo_coma))
print("Los espacios son {}" .format(n_signo_espacio))
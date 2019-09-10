# Crear un progra que cuente el numero de vocales y con sonantes dentro de una frase introducida por el usuario

frase_del_usuar = input("introduce una frase: ").upper()

vocales = ["A", "E", "I", "O", "U"]

n_vocales = 0
n_consunantes = 0

for letra in frase_del_usuar:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consunantes += 1

print("Las vocales son {}" .format(n_vocales))
print("Las consunantes son {}" .format(n_consunantes))
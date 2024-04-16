lista = []
if_fin = False
cant_a = 0
cant_e = 0

while if_fin == False:
    nombre = input("Ingrese un nonmbre en especifico:")
    lista.append(nombre)

    if nombre == "fin":
        if_fin = True
        lista.remove("fin")

    if nombre[0] == "a":
        cant_a += 1
    if nombre[0] == "A":
        cant_a += 1
    if nombre[0] == "e":
        cant_e += 1
    if nombre[0] == "E":
        cant_e += 1

lista.sort()

print(f"Los nombres ingresados fueron: {lista}")
print(f"La cantidad de nombres que empiezan con A son: {cant_a}")
print(f"La cantidad de nombres que empiezan con E son: {cant_e}")



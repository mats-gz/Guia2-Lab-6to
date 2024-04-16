#fruta ej 5
frutas = ["manzana", "banana", "naranja", "kiwi", "melón", "fresa", "piña"]

print("Estas son las frutas en su lista")
for fruta in frutas:
    print(fruta)


#fruta ej 5.1
numFrutas = int(input("Ingrese la cantidad de frutas que quiere meter en su lista:"))
numAux = 0

while (numAux < numFrutas):
    fruta = input(f"Ingrese su fruta nº{numAux + 1}:")
    frutas.append(fruta)
    numAux += 1


#fruta ej 5.2
frutaLista = input("Ingrese la fruta q desea encontrar en la lista:")

if frutaLista in frutas:
    print(f"La fruta {frutaLista} si esta en la lista.")
else:
    print(f"La fruta {frutaLista} no esta en la lista.")
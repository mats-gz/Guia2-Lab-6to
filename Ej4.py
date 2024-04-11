import random 
frutas = ["manzana", "banana", "naranja", "uva", "sandía", "pera", "kiwi", "melón", "fresa", "piña"]

def contador(frutas):
    elem1 = random.choice(frutas)
    elem2 = random.choice(frutas)
    elem3 = random.choice(frutas)

    rebanada = elem1[1 : len(elem1) - 1]
    print("Algunos elementos de la lista:", elem1, elem2, elem3, "Una rebanada de un elemento:", rebanada)

contador(frutas)
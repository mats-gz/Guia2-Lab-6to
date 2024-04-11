#pt1
num = 0

while (num <= 4):
    print(num)
    num += 1

#pt2
sumaTotal = 0

def numConsola(sumaTotal):

    num = int(input("Ingrese un número: "))

    if num < 0:
        print("El num ingresado es negativo, la suma total de todos los numeros positivos ingresados es:", sumaTotal)
        exit()

    sumaTotal += num

    while (num >= 0):
         numConsola(sumaTotal)

numConsola(sumaTotal)



    

color = input("Ingrese su color favorito:")

def mensColor(color):
    colorUser = color.lower()
    if colorUser == "verde":
        print("El color introducido fue verde")
    elif colorUser != "verde":
        print("Su color introducido es:", color)

mensColor(color)


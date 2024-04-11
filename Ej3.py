import random
cad = "reversa"

def caracteresCad(cad):
    numFinal = len(cad) - 1
    numRandom = random.randint(1, len(cad) - 1)
    
    primerTerm = cad[0]
    ultTerm = cad[numFinal]
    randomTerm = cad[numRandom]
    rebanada = cad[2:4]

    print("Primer termino:", primerTerm, "Ultimo termino:", ultTerm, "Termino random:", randomTerm, "Una rebanada de cadena", rebanada)

caracteresCad(cad)
        

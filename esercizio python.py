def sceltaquad(): 
    print("Definisci un lato del quadrato")
    lato = input()
    print("Il perimetro risulta " + str(int(lato) * 4))  

def sceltacer(): 
    print("Definisci il raggio del cerchio")
    raggio = input()
    print("La circonferenza è " + str(2 * 3.14 * int(raggio)))  

def sceltarett():  
    print("definisci base e altezza")
    base = input()
    altezza = input()
    print("Il perimetro è " + str(int(base) * 2 + int(altezza) * 2))  


print("Benvenuto, premi 1 per avviare il programma")
selection = input()
if int(selection) == 1:
    print("Premi il tasto 1 per avviare il perimetro di un quadrato, 2 per la circonferenza di un cerchio e 3 per il perimetro di un rettangolo")
    sceltacalc = input()
    if int(sceltacalc) == 1:
        sceltaquad()
    elif int(sceltacalc) == 2:
        sceltacer()
    elif int(sceltacalc) == 3:
        sceltarett()
else:
    print("Ma come pretendi di fare questi calcoli matematici se non riesci nemmeno a premere un numero?")

      
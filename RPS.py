import random


while True:
    kayttaja = input("Valitse: kivi, sakset vai paperi? ")
    mahdolliset_valinnat = ["kivi", "sakset", "paperi"]
    tietokone = random.choice(mahdolliset_valinnat)

    print(f"\nSinä valitsit {kayttaja}, tietokone valitsi {tietokone} \n")

    if kayttaja == tietokone:
        print("Tasapeli")
    elif kayttaja == "sakset":
        if tietokone == "paperi":
            print("Voitit!")
        else:
            print("Hävisit!")
    elif kayttaja == "paperi":
        if tietokone == "sakset":
            print("Hävisit!")
        else:
            print("Voitit!")
    elif kayttaja == "kivi":
        if tietokone == "paperi":
            print("Hävisit!")
        else:
            print("Voitit!")
    uudelleen = input(print("Pelataanko uudelleen? (k/e)?"))
    if uudelleen == "e":
        break
paspoortcheck = input("Heeft U een paspoort? Ja of Nee: ")
leeftijd = int(input("Wat is uw leeftijd?: "))


if paspoortcheck == 'Ja' and leeftijd >= 18:
    print("U mag stemmen!")


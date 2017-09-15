paspoortcheck = input("Heeft U een paspoort?: ")
leeftijd = int(input("Wat is uw leeftijd?: "))


if paspoortcheck == 'Ja' and leeftijd >= 18:
    print("U mag stemmen!")

else:
    print("U mag nog niet stemmen")
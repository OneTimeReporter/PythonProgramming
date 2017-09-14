paspoortcheck = input("Heeft U een paspoort? True of False: ")
leeftijd = int(input("Wat is uw leeftijd?: "))


if paspoortcheck == 'True' and leeftijd >= 18:
    print("U mag stemmen!")


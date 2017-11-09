
maand = int(input('Maand: '))

def seizoen(maand):
    if maand >= 0 and maand <=2:
        antwoord = 'Winter'
    elif maand >= 3 and maand <=5:
        antwoord = 'Lente'
    elif maand >= 6 and maand <=8:
        antwoord = 'Zomer'
    elif maand >= 9 and maand <=11:
        antwoord = 'Herfst'
    else:
        antwoord = 'Error'
    return antwoord

print(seizoen(maand))
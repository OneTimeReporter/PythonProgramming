letterlijst = ['a','b','c']

def wijzig(leterlijst):

    letterlijst.clear()
    letterlijst.append('e')
    letterlijst.append('f')
    letterlijst.append('g')





print(letterlijst)
wijzig(letterlijst)
print(letterlijst)

#1. Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
#1-Antwoord: Dan wordt letterlijst alleen veranderd binnen de functie, en er is geen return waarde
#2.Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
#2.Antwoord: Nee, ik heb gebruik gemaakt van .append, dat werkt alleen met lists.
#3.Welke rol speelt (im)mutabiliteit in deze vraag?
#3-Antwoord: Als je het niet juist doet, zal Python gewoon de variabelnaam verbinden met de originele waarde en zal de gedefinieerde waarde geen variabelenaam hebben om mee opgeroepen te worden.


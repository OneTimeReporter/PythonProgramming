
def gemiddelde():
    zin = input('Vul uw willekeurige zin in: ')
    x = zin.split(' ')
    y = zin.replace(' ','')
    z = (len(y) / len(x))
    antwoord = 'Uw zin bestaat uit %s woorden.\nIn totaal zijn al deze woorden bij elkaar %s letters.\nUw zin heeft gemiddeld %s letters per woord' %(len(x), len(y), z)
    print(antwoord)
gemiddelde()
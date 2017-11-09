

def sorter():
    lijst = []
    vierletterlijst = []

    for x in range(0,10):
        x = str(input('Geef lijst met minimaal 10 strings: '))
        lijst.append(x)
    print(lijst)

    for item in lijst:
        if len(item) == 4:
            vierletterlijst.append(item)
    x= 'De nieuw-gemaakte lijst met alle vier-letter strings is : %s' % (vierletterlijst)
    return x

print(sorter())

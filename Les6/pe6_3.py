invoer = "5-9-7-1-7-8-3-2-4-8-7-9"


def machine(invoer):
    a = invoer.split('-')
    b = [int(i) for i in a]
    c = sorted(b)
    d = max(b)
    e = min(b)
    f = len(b)
    g = sum(b)
    h = (g/f)
    z = 'Gesorteerde list van ints: %s \n Grootste getal : %s , en het kleinste getal : %s \n Aantal getallen: %s , Som van de getallen : %s \n Gemiddelde: %s ' % (c,d,e,f,g,h)
    print(z)
machine(invoer)

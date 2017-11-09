infile = open('kaartnummers.txt')
lines = infile.readlines()

def regelteller():
    a = len(lines)
    b = 'Deze File is %s regels lang.'%(a)
    return b

def maxgetal():
    y = []
    for line in lines:
        x = line.strip('\n').split(',')
        y.append(int(x[0]))
    maximum = max(y)
    locatie = y.index(max(y)) +1
    z = 'Het grootste kaartnummer is %s en dat staat op regel %s ' % (maximum, locatie)
    return z
print(maxgetal())



print(regelteller())


infile.close()
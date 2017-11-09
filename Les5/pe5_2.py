infile = open('kaartnummers.txt')
lines = infile.readlines()

for line in lines:
    x = line.strip('\n').split(',')
    print(x[1],' heeft kaartnummer: ', x[0])

infile.close()

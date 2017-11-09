outline = open('hardlopers.txt', 'a')


import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y , %H:%M:%S, ")
naam = input('Naam van hardloper? ')

outline.write(s + naam + '\n')
counter = 0
aantal = 0


while True:
    x = int(input("Geef een getal\n"))

    if x != 0:
        counter +=1
        aantal +=x
    else:
        print("Er zijn " + str(counter) + " getallen ingevoerd, de som is: " + str(aantal))

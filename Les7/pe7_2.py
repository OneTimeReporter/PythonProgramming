while True:
    x = input("Voer uw woord in:\n")

    if len(x) != 4:
        print(x + " heeft " + str(len(x)) + " letters")
    else:
        print("Inlezen van de correcte string: " + x + " is geslaagd.")
        break
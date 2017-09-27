inputwaarde = input("Vul input in: ")


def acronym(inputwaarde):
    temp = inputwaarde.split(' ')
    returnvalue = ""
    for char in temp:
        returnvalue += char[0]
    return returnvalue.upper()

print(acronym(inputwaarde))
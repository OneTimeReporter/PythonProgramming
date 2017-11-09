def code(invoerstring):
    result = ""
    for char in invoerstring:
        x = ord(char) + 3
        result += chr(x)
    print(result)



code(input("invoerstring AUB: \n"))






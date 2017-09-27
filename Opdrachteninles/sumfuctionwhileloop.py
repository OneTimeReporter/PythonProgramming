
def sum():
    total = 0
    while True:
        nextint = (input('Next int: '))
        if nextint == 'quit':
            break
        else:
            total += int(nextint)
        print(total)

sum()




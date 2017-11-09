d = {}
with open('tickerfile') as f:
    for line in f:
        key, value = line.strip().split(':')
        d[key] = (value)
print(d)
x = input("Voer company naam in: \n")



for key, value in d.items():
    if x in key:
        print(value)
    else:
        print("Is er niet")
        break
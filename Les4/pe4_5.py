grondtallen = [3,4,5,-12]

def kwadraten_som(grondtallen):
    for num in grondtallen:
        if num <=0:
            grondtallen.remove(num)
    squared = [x**2 for x in grondtallen]
    result = sum(squared)
    return result

print (kwadraten_som(grondtallen))





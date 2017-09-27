def convert(celcius):
    fahrenheitconvert = (celcius * 1.8 ) +32
    return fahrenheitconvert



def table():
    print('F        C')
    for i in range(-30, 50, 10):
        print(convert(i), i, sep='       ')

table()
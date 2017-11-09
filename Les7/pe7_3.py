dict = {"a": 5,
        "b": 7,
        "c":3,
        "d":9,
        "e":10,
        "f":9,
        "g":9,
        "h":9}


for key, value in dict.items():
    if value >= 9:
        print(key,value)
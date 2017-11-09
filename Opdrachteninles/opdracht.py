x = 2
y = 5


def fun():
    y = 3
    global x
    x = 1
    print(x*y, end = ' ')
    return x*y



x = fun()
print(x*y, end = ' ')



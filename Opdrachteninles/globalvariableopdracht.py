def f(b):
    global a
    a = 6
    return a*b

a = 0
print('f(3) = {}'.format(f(3)))
print('a is {}'.format(a))
x = 1
y = 4
def fun():
 x = 2
 global y
 y = 3
 print(y, end = ' ')
fun()
print(y, end = ' ')

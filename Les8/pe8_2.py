import random

def dice():
    roll = random.randint(1, 6)
    return roll

def monopolyworp():
     x = dice()
     y = dice()
     sum = x+y
     print (str(x) + "+"  +str(y)+ "=" +str(sum))
     if x == y:
         x = dice()
         y = dice()
         sum = x + y
         print(str(x) + "+" + str(y) + "=" + str(sum))
         if x == y:
             x = dice()
             y = dice()
             sum = x + y
             print(str(x) + "+" + str(y) + "=" + str(sum))
             if x ==y :
                 print("Gevangenis")
monopolyworp()
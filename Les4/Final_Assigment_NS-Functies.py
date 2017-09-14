
#afstandKM = 50
#leeftijd = 30
#weekendrit = True

def standaardprijs(afstandKM):
    if afstandKM >= 50:
        basePrice = 15 + afstandKM*0.60
    elif afstandKM <= 0:
        basePrice = 0
    else:
        basePrice = 0.80* afstandKM
    return basePrice

def leeftijdscheck(leeftijd):
    if leeftijd >= 65 or leeftijd < 12:
        return True
    else:
        return False

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijdscheck(leeftijd) == True and weekendrit == True:
        farePrice = standaardprijs(afstandKM) - ((standaardprijs(afstandKM) / 100) * 35)
    elif leeftijdscheck(leeftijd) == True and weekendrit == False:
        farePrice = standaardprijs(afstandKM) - ((standaardprijs(afstandKM) / 100) * 30)
    elif leeftijdscheck(leeftijd) == False and weekendrit == True:
        farePrice = standaardprijs(afstandKM) - ((standaardprijs(afstandKM) / 100) * 40)
    else:
        farePrice = standaardprijs(afstandKM)
    return farePrice


print(ritprijs(10,False,50))   # checkt de ritprijs met 30% korting.
print(ritprijs(10,True,50))    # checkt de ritprijs met 35% korting.
print(ritprijs(23,True,50))    # checkt de ritprijs met 40% korting.
print(ritprijs(23,False,50))   # checkt de ritprijs zonder korting.

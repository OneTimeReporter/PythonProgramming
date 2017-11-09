

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]



def gemiddelde_per_student(studentencijfers):
    antw =[]
    for row in studentencijfers:
        a = ((sum(row)) / len(row))
        antw.append(a)

    return antw



def gemiddelde_van_alle_studenten(studentencijfers):
    list = []
    for row in studentencijfers:
        a = sum(row)
        b = len(row)
        c = len(studentencijfers)
        list.append(a)
    antw = (sum(list) / (b*c) )

    return antw


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
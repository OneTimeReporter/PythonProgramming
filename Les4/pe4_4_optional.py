oldpassword = input("Uw oude wachtwoord a.u.b: ")
newpassword = input("Uw nieuwe wachtwoord a.u.b: ")

def contains_digit(x):
    return any(char.isdigit() for char in newpassword)
print(contains_digit(newpassword))
#functie dat checkt of het nieuwe wachtwoord een nummer bevat



def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6 and contains_digit(newpassword) == True :
        return True
    else:
        return False


if new_password(oldpassword,newpassword) == True:
    print("Wachtwoord gewijzigd!")
else:
    print("U heeft iets fout gedaan, uw nieuwe wachtwoord mag niet uw oude wachtwoord zijn, en uw wachtwoord moet langer dan 6 karakters lang zijn.")
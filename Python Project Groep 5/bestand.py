import mysql.connector
from mysql.connector import Error
from random import *
import time
import pyotp

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mydb',
                                       user='root',
                                       password='admin')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()

def createaccount():
    cnx = mysql.connector.connect(host='localhost', user='root', database='mydb', password='admin')
    cursor = cnx.cursor()

    authenticator_code = authenticator()
    nieuwusername = input("Vul een gewenste username in\n")
    nieuwwachtwoord = input("Vul een gewenste wachtwoord in\n")
    nieuwvoornaam = input("Vul uw voornaam in\n")
    nieuwachternaam = input("Vul een achternaam in\n")

    try:
        cursor.execute("INSERT INTO persoon (Username, Password, Voornaam, Achternaam, authen_key) VALUES (%s,%s,%s,%s,%s)",
                       (nieuwusername, nieuwwachtwoord, nieuwvoornaam, nieuwachternaam,
                        authenticator_code))  # voegt nieuwe gebruiker in het systeem
        print("Account gemaakt!")
        print("Uw authenticator code is: " + authenticator_code + " .\nVoer deze code in op Google Authenticator!")
        print("U wordt nu teruggestuurd naar het hoofdmenu.")
        userexistscheck()
    except mysql.connector.errors.IntegrityError:
        print('Username is al in gebruik!')  # systeem error melding
        createaccount()
    emp_no = cursor.lastrowid
    cnx.commit()
def inlog():

    #Inlogsysteem, vraagt of de gebruiker al een account heeft
    cnx = mysql.connector.connect(host = 'localhost', user='root', database='mydb', password='admin')
    cursor = cnx.cursor()
    c = cnx.cursor()
    usernameinput = input("Uw username aub:\n")
    wachtwoordinput = input("Uw wachtwoord aub:\n")

    correctwachtwoord = cursor.execute("SELECT Password, Username, idPersoon, authen_key FROM persoon WHERE Username = '%s';"% usernameinput)
    x = cursor.fetchone()
    userexistscheck = c.execute("SELECT COUNT(Username) FROM persoon WHERE Username = '%s';" % usernameinput)
    y = c.fetchone()

    if y[0] == 0:
        print("Deze gebruiker bestaat niet.")
        inlog()
    elif x[0] == wachtwoordinput and x[1] == usernameinput:
        vraag = input("Vul uw Google Authenticator code in:\n")
        totp = pyotp.TOTP(x[3])
        if vraag == totp.now():
            print('U bent ingelogd, welkom in het systeem!')
            persoonsID = x[2]
            print(str(persoonsID) + ": Uw persoonsID")
            fiets(persoonsID)
        else:
            print("Uw Authenticator code klopt niet.")
            inlog()
    else:
        print('Uw username en/of wachtwoord klopt niet, probeer opnieuw.')
        inlog()

    #gebruiker wordt aangemaakt
def fiets(persoonsID): #Fiets wordt automatisch geregistreerd met de PersoonsID van de inlogger
    cnx = mysql.connector.connect(host='localhost', user='root', database='mydb', password='admin')
    cursor = cnx.cursor()
    randomnumber = randint(1,1000000)  #geeft fietsID een ID tussen 1 en 100, geen idee of het automatisch al gebruikte nummers vermijd, zo niet dan moet daar iets tegen geimplementeerd worden


    fietsID_check = input("Heeft uw fiets al een ID? Ja/Nee:\n")
    if fietsID_check =="Nee": #Fiets krijgt zijn 'stikkertje' in de vorm van een fiets ID code
        fietstype = input("Wat voor een soort fiets heeft u?\n")
        cursor.execute("INSERT INTO Fiets (idFiets,type,Persoon_idPersoon) VALUES (%s,%s,%s)",
                       (randomnumber,fietstype,persoonsID))#fiets wordt geinsert in de fiets tabel van de database
        print("Fiets geregistreerd!")
        print("Uw fiets ID is : " + str(randomnumber) + " , vergeet het niet.")
        emp_no = cursor.lastrowid
        cnx.commit()


        timestamp_create = time.strftime('%c') #timestamp geeft jaar maand dag, de datatype van timestamp moet in de database veranderd worden om een andere formaat te gebruiken maar ik krijg errors
        cursor.execute("INSERT INTO stalling (fiets_status, timestamp, Fiets_idFiets, Fiets_Persoon_idPersoon) VALUES (%s,%s,%s,%s)",
                       (0,timestamp_create,randomnumber,persoonsID))
        emp_no = cursor.lastrowid
        cnx.commit()
        print("Data opgeslagen, fiets is niet in stalling op het moment.") #Ik ga er van uit dat de fiets niet in de stalling zit op het moment van registratie.

    else: #in principe het enige wat deze stuk code doet is in en uithalen van de fiets, er is ook een check zodat de persoon alleen zijn eigen fiets kan pakken
        stalling = input("Voer a.u.b uw fiets ID in:\n")
        cursor.execute("SELECT fiets_status, Fiets_Persoon_idPersoon FROM stalling WHERE Fiets_idFiets = '%s';" % stalling)
        y = cursor.fetchone()

        if y[1] != persoonsID:
            print("DIT IS NIET UW FIETS")
        elif y[0] == 0:
            cursor.execute("UPDATE stalling SET fiets_status = '1'")
            emp_no = cursor.lastrowid
            cnx.commit()
            print("Dank u wel voor het gebruik van onze stallingen, uw fiets zit nu veilig in onze stalling")
        elif y[0] == 1:
            cursor.execute("UPDATE stalling SET fiets_status = '0'")
            emp_no = cursor.lastrowid
            cnx.commit()
            print("Nog een fijne dag, uw fiets is nu uit de stalling")
def authenticator():
    randomkey = pyotp.random_base32()
    return randomkey
def userexistscheck():
    cnx = mysql.connector.connect(host='localhost', user='root', database='mydb', password='admin')
    cursor = cnx.cursor()
    userCheck = input("Bent u al een klant?: Ja/Nee\n")

    if userCheck != "Ja" and userCheck != "Nee":
        print("Vul alstublieft Ja of Nee in.")
        userexistscheck()
    if userCheck == "Ja":
        inlog()
    else:
        createaccount()

userexistscheck()



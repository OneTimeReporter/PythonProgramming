lengte = eval(input("Wat is uw lengte in meters?: "))
gewicht = int(input("Wat is uw gewicht in kilo's?: "))



def BMI(lengte, gewicht):

    bmistatus = (gewicht / (lengte**2))

    if bmistatus <= 18.5:
        bmistatus = "Underweight"
    elif bmistatus >= 25:
        bmistatus = "Overweight"
    else:
        bmistatus = "Normal"
    return bmistatus

print(BMI(lengte,gewicht))

print(BMI(190,70))
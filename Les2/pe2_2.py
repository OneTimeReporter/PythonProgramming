cijferICOR = 7
cijferPROG = 8
cijferCSN = 8
cijferlijst = [cijferPROG,cijferICOR,cijferCSN]

gemiddeldeCijfer = float((cijferCSN + cijferICOR + cijferPROG) / 3)
beloning = int(sum(cijferlijst) * 30)
overzicht = 'Mijn cijfers (gemiddeld een '+ str(gemiddeldeCijfer)+ ') leveren een beloning van ' +str(beloning)+ ' Euro op!'

print(overzicht)



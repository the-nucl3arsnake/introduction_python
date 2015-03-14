#programme pour voir si une année est bissextile

#Saisie de l'année
annee_test = input("Quelle année voulez-vous tester? ")
annee_test = int(annee_test)

#Vérification
if annee_test%4 == 0 and annee_test%100==0  and annee_test%400==0:
	print("L'année ",annee_test," est bissextile")
else:
	print("L'année ",annee_test, "n \'est pas bissextile")

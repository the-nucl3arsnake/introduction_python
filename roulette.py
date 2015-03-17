# Programme de roulette de casino
import random
import math

# Définition du nombre de crédits du joueur
credit = input("Combien de Crédits avez-vous? ")
try:
	credit = int(credit)
except ValueError:
	print("Veuilliez saisir un chifre.")
except:
	print("Une erreur est survenue. Contactez votre administrateur")

# ligne de debug
#print (type(credit))

while credit > 0:
# pari du joueur
	pariChiffre = input("Sur quel chiffre voulez-vous parier? (0-49)")
	try:
		pariChiffre =int(pariChiffre)
	except ValueError:
		print("Veuillez saisir un chiffre.")
	except:
		print("Une erreur est survenue. Contactez votre administrateur.")
		
	pariArgent = input("Combien voulez-vous parier? ")
	try:
		pariArgent =int(pariArgent)
	except ValueError:
		print("Veuillez saisir un chiffre.")
	except:
		print("Une erreur est survenue. Contactez votre administrateur.")
		
# generation du nombre aleatoire
	nbreAlea = random.randrange(0,49)
	print("Le nombre tiré au sort est :",nbreAlea)
	
# Verification gain
	if nbreAlea == pariChiffre:
		victoire = True
	if pariChiffre % 2 == 0 and nbreAlea % 2 == 0:
		doublePair = True
	if pariChiffre % 2 == 1 and nbreAlea == 1:
		doublePair = False
		
	if victoire = True:
		credit = pariArgent * 3
		print(" Bravo, vous avez gagné. Il vous reste",credit, "credits")
	elif doublePair = True or doublePair = False:
		pariArgent = pariArgent / 2
		credit = math.ceil(credit - pariArgent)
		print("Demi-victoire. il vous reste: ",credit," credits." )
	else:
		credit = credit - pariArgent
		print("Désolé vous avez perdu. Il vous reste: ",credit," credits")
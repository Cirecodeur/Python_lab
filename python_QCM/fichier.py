import os
import math
import random
#aFFICHE LES SUGGESTIONS (TOUS SAUF LES PREMIERS ET DERNIER ELEMENTS)
def printsugestion(list):
	for i in list:
		if i != 0 and i != list[-1]:
			print i,"\n"
#end function
#affiche la reponse et non le chiffre correspondant 
def printAnswer(list):
	list = list.split(":")
	return list[-1]
#end function
#affiche le chiffre correspondant a la reponse 
def printAnswerN(list):
	list = list.split(":")
	return int(list[0])
#end function

#lance le jeu 
def lance(question, indice):
	
			# SPLIT POUR DECOUPER LA CHAINE EN TABLLEAU A PARTIR DU ;
			question = question[indice].split(";")
			#print(question[0])
			printsugestion(question)
			rep2 = 0
			while rep2 not in (1, 2, 3):
				rep2 = input("Quelle est la reponse ?")
			if(rep2 == printAnswerN(question[-1])):
				print ": Bravo, c'est une bonne reponse"
				return 1
			else:
				print "Desole, c'est une mauvaise reponse.Il fallait choisir la reponse ",printAnswerN(question[-1])
				return 0

#print "le chemin est ",os.getcwd()rep = False
def choseDomain():
	fichier = os.getcwd() #chemin du repertoire courant

	rep = False
	while rep == False :
		print("*********************************\n\n\t\t\t\t**")
		print("**Bienvenue dans TopQuiz **\n\t\t\t\t**\n**\n")
		print("*********************************\n")
		print("Veuillez choisir une section")
		choix = int(input("1  : HISTOIRE\n2  : SCIENCE\n3  : PROGRAMMATION\n"))
		choixListe = (1, 2, 3)
		rep = choix in choixListe
	if(choix == 1):
		fichier+="\Histoire.txt"
	elif(choix == 2):
		fichier+="\Science.txt"
	else:
		fichier+="\Culture.txt"
	fichier  = open(fichier, 'r')
	question = fichier.readlines()
	return question

#fin
def aleat_generate(maListe):
	return random.randrange(0, len(maListe))
#fin
quitter = ""
while quitter != "Q":
	question = choseDomain()
	essai = 1
	sum = 0
	while essai <=5:
		indice = aleat_generate(question)
		sum += lance(question,indice)
		essai+=1
		del question[indice]
	else:
		print "Termine vous avez : {0}/{1}".format(sum, essai-1)
	#print fichier
	quitter = raw_input("Entrer q ou Q pour quitter sinon Appuyer sur une Touche\n").upper()
	if quitter == "Q":
		print "Vous avez decidez de quitter le Jeu ---- Aurevoir"
	print "\n\n\n\n\n\n\n\n"

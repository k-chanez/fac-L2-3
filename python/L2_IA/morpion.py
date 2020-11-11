
from math import inf as inf
import copy 
tableau_initial = [0,0,0,
                   0,0,0,
                   0,0,0]
longeur = 3
largeur = 3

def verifier_case_vide(tab,i):
    if not tab[i]:
        return True
    return False

def placer_piece(tab,x,joueur):
    if(verifier_case_vide(tab,x)):
        tab[x] = joueur

def cases_vides(tab):
    resultat = []
    for i in range(len(tab)):
        if(verifier_case_vide(tab,i)):
            resultat.append(i)
    return resultat;

def successeurs(tab, joueur):
    etat_accessible = []
    cases_possible = cases_vides((tab))

    for i in cases_possible:
        temp = tab.copy()
        placer_piece(temp,i,joueur)
        etat_accessible.append(temp)
    return etat_accessible

def fonction_decision_H(tableau, joueur):
	cas_victoire = [
	#alignement en ligne
		[tableau[0], tableau[1], tableau[2]],
		[tableau[3], tableau[4], tableau[5]],
		[tableau[6], tableau[7], tableau[8]],
	#alignement en colonne
		[tableau[0], tableau[3], tableau[6]],
		[tableau[1], tableau[4], tableau[7]],
		[tableau[2], tableau[5], tableau[8]],
	#alignement en diagonale
		[tableau[0], tableau[4], tableau[8]],
		[tableau[2], tableau[4], tableau[6]],
	]
	if [joueur,joueur,joueur] in cas_victoire:
		return True
	return False

def nbAlign(p,J,i):
    compteur = 0
    resultat = 0
    #alignement en ligne
    for a in range(longeur):
        for j in range(largeur):
            if p[a*longeur+j] == J:
                compteur+=1
            elif p[a*longeur+j] == -1*J:
                compteur = -inf
        if compteur == i:
            resultat+=1
        compteur = 0
	
    #alignement en colonne
    for a in range(longeur):
        for j in range(largeur):
            if p[a+j*longeur] == J:
                compteur+=1
            elif p[a+j*longeur] == -1*J:
                compteur = -inf
        if compteur == i:
            resultat+=1
        compteur = 0
    #alignement en diagonale1
    for a in range(longeur) :
        if p[a*longeur+a] == J:
            compteur+=1
        elif p[a*longeur+a] == -1*J:
            compteur = -inf
    if compteur == i:
            resultat+=1
    compteur = 0
    #alignement en diagonale2
    for a in range(1,longeur+1):
        if p[a*longeur-a] == J:
            compteur+=1
        elif p[a*longeur-a] == -1*J:
            compteur = -inf
    if compteur == i:
            resultat+=1
    compteur = 0

    return resultat

def fonction_evaluation_F(p):
    if fonction_decision_H(p,1):
        resultat = inf
    elif (fonction_decision_H(p,-1)):
        resultat = -inf
    else:
        resultat = (3* nbAlign(p,+1,2) + nbAlign(p,+1,1)) - (3* nbAlign(p,-1,2)+ nbAlign(p,-1,1))
    return resultat

def minimax(n,p,joueur):
	if fonction_decision_H(p[0],1):
		return [p[0], inf]
	elif (fonction_decision_H(p[0],-1)):
		return [p[0], -inf]
	elif(n == 0):
		return [p, 0]
	else:
		s = successeurs(p[0],joueur)
		pile = []
		index = 0
		mx = -inf if joueur == 1 else inf
		i = 0
		for su in s:
			t = fonction_evaluation_F(su)
			if(joueur == 1):
				if t > mx:
					mx = t
					index = i
			else:
				if t < mx:
					mx = t
					index = i			
			pile.append(t)
			i+=1
		if joueur == 1:
			return [s[index], minimax(n-1,[s[index], max(pile)],-1)[1]]
		else :
			return [s[index], minimax(n-1,[s[index], min(pile)],1 )[1]]


def afficher(tab):
    print(tab[:3])
    print(tab[3:6])
    print(tab[6:])
    print()

print("debut de jeux ")
afficher(tableau_initial)
j = 1
resultat = minimax(9,[tableau_initial, 0],j)

for i in range(largeur*longeur):
	print("joueur" ,(i%2) + 1,"a joué" )	
	afficher(resultat[0]) 	
	j *= -1
	resultat = minimax(min(9, largeur*longeur-i-1), resultat, j)
if( resultat == inf ):
	print("joueur 1 gagné")
elif( resultat == -inf ):
	print("joueur 2 gagné")
else:
	print("personne a gagné match nul ")


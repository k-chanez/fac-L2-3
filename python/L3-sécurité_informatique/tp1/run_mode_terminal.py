from termcolor import colored ,cprint 
import tp1
import os, random, struct
import sys
import os.path
import string

iv = (random.randint(0, 100)) 

def menu():
	cprint(" _^'^'^'^'^'^'^'^'^'^'^_MENU_ ^'^'^'^'^'^'^'^'^'^'^'^_",'red','on_cyan')
	cprint("1. chiffrer une lettre",'cyan')
	cprint("2. dechiffrer la lettre",'cyan')
	cprint("3. chiffrer un message dans un fichier en mode ECB",'blue')
	cprint("4. dechiffrer un message dans un fichier en mode ECB",'blue')
	cprint("5. chiffrer un message dans un fichier en mode CBC",'green')
	cprint("6. dechiffrer un message dans un fichier en mode CBC",'green')
	cprint("7. chiffrer un message dans un fichier en mode CFB",'yellow')
	cprint("8. dechiffrer un message dans un fichier en mode CFB",'yellow')
	cprint("9. chiffrer un message dans un fichier en mode OFB",'red')
	cprint("10. dechiffrer un message dans un fichier en mode OFB",'red')
	cprint("0. quitter ",'magenta')
def mini_menu():
	cprint("-----------------_MINI_MENU_--------------------",'red','on_cyan')
	print("1.souhaitez-vous revenir en menu principal")
	print("0.quitter ")
def main():
	menu()
	choix = input("Choix : ")
	while menu !='0':
		if choix == '0':
		 	cprint("Au Revoir",'blue')
		 	break 
		if choix == '1':
			a=input("saisie une lettre : ")
			b=input("saisie la 1er paire de clef k[0] (?,) : ")
			c=input("saisie la 2éme paire de cl1f k[1] (,?) : ")
			k1 = int(b)
			k2 = int(c)
			c
			print(colored('le chiffré => ','red'),(tp1.enc_byte(a,(k1,k2))))
			mini_menu()
			choix = input("Choix : ")
			if choix == '1':
				menu()	
				choix = input("Choix : ")
			else :
				cprint("Au Revoir",'blue') 
				break
		if choix == '2':
			tmp=input("Avant de passer au déchiffrement <Vous êtes sûr d'avoir passé par le chiffrement et souvenez-vous de la clé>(y/n) : " )
			if tmp =="y":
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de cl1f k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				m =tp1.enc_byte(a,(k1,k2))
				print(colored("dechiffré => ",'red'),tp1.dec_byte(m,(k1,k2)))
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else: 
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
		if choix == '3':
			file=input("saisie le nom de fichier exp <file.txt> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.enc_file(file,(k1,k2))
				cprint("le chiffrement validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else : 
				print("Erruer : le fichier ne exist pas verifier vous bien ")
				menu()
				choix = input("Choix : ")
		if choix == '4':
			file=input("saisie le nom de fichier exp <file.txt.enc> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.dec_file(file,(k1,k2))
				cprint("le dechiffrement est validé", 'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else :
				print("Erruer le fichier ne exist pas vous devrez passe par le chiffrement (choix 3) pour avoir le fichier .enc")
				menu()
				choix = input("Choix : ")
		if choix == '5':
			file=input("saisie le nom de fichier exp <CBC.txt> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.enc_file_cbc(file,(k1,k2),iv)
				cprint("le chiffrement est validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break	
			else : 
				print("Erruer : le fichier ne exist pas verifier vous bien ")
				menu()
				choix = input("Choix : ")
		if choix == '6':
			file=input("saisie le nom de fichier exp <CBC.txt.enc> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.dec_file_cbc(file,(k1,k2),iv)
				cprint("le dechiffrement est validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else :
					print("Erruer le fichier ne exist pas vous devrez passe par le chiffrement CBC (choix 5) pour avoir le fichier .enc")
					menu()
					choix = input("Choix : ")
		if choix == '7':
			file=input("saisie le nom de fichier exp <CFB.txt> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.enc_file_cfb(file,(k1,k2),iv)
				cprint("le chiffrement est validé",'yellow')
				cprint("-----------------_MINI_MENU_--------------------",'red','on_cyan')
				print("1.souhaitez-vous revenir en menu principal")
				print("0.quitter ")
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else : 
				print("Erruer : le fichier ne exist pas verifier vous bien ")
				menu()
				choix = input("Choix : ")
		if choix == '8':
			file=input("saisie le nom de fichier exp <CFB.txt.enc> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.dec_file_cfb(file,(k1,k2),iv)
				cprint("le dechiffrement est validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else :
					print("Erruer le fichier ne exist pas vous devrez passe par le chiffrement CFB (choix 7) pour avoir le fichier .enc")
					menu()
					choix = input("Choix : ")
		if choix == '9':
			file=input("saisie le nom de fichier exp <OFB.txt> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.enc_file_ofb(file,(k1,k2),iv)
				cprint("le chiffrement est validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else : 
				print("Erruer : le fichier ne exist pas verifier vous bien ")
				menu()
				choix = input("Choix : ")	
		if choix == '10':
			file=input("saisie le nom de fichier exp <OFB.txt.enc> " )
			if os.path.isfile(file):
				b=input("saisie la 1er paire de clef k[0] (?,) : ")
				c=input("saisie la 2éme paire de clef k[1] (,?) : ")
				k1 = int(b)
				k2 = int(c)
				tp1.dec_file_ofb(file,(k1,k2),iv)
				cprint("le dechiffrement est validé",'yellow')
				mini_menu()
				choix = input("Choix : ")
				if choix == '1':
					menu()	
					choix = input("Choix : ")
				else :
					cprint("Au Revoir",'blue') 
					break
			else :
					print("Erruer le fichier ne exist pas vous devrez passe par le chiffrement OFB (choix 9) pour avoir le fichier .enc")
					menu()
					choix = input("Choix : ")
main()

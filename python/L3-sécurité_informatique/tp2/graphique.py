from tkinter import * 
from tkinter import filedialog 
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os,random,struct,sys ,string,os.path
from termcolor import colored ,cprint
from tkinter import messagebox 
from Crypto.Util.number import getPrime, inverse 
from math import gcd 
import os 
import ssl, socket
import hashlib,tp2


last_bits = 256 
A_prive, A_public = tp2.gen_rsa_key(last_bits)

# c'est pour ecrire au clavie le nombre de bits pour générer une clé 
'''def gen():
	global A_prive, A_public, last_bits
	new_bits = last_bits
	if entrybits.get() != "":
		new_bits = int(entrybits.get(),10)
	if last_bits != new_bits :
		last_bits = new_bits
		A_prive, A_public = tp2.gen_rsa_key(new_bits)

	return A_prive, A_public'''

#A_prive,A_public = tp2.gen_rsa_key(256)
def affiche_enc():
	k0 = int(entryK0.get(),10)
	k1 = int(entryK1.get(),10)
	Message = entryMessage.get()
	m = tp2.rsa_enc(Message,(k0,k1))
	lblResult_enc["text"]= "Chiffrer = "+ str(m)
	entryMessage.config(state=DISABLED)

def affiche_dec():
	entryMessage.config(state=NORMAL)
	k0 = int(entryK0.get(),10)
	k1 = int(entryK1.get(),10)
	m = int(lblResult_enc["text"][11:len(lblResult_enc["text"])])
	lblResult_enc["text"]= "Déchiffrer = "+ str(tp2.rsa_dec(m,(k0,k1)))

def gen_key_Public():	
	#A_prive,A_public = gen()
	entryK0.config(state=NORMAL)
	entryK0.insert(END, A_public[0])
	entryK1.config(state=NORMAL)
	entryK1.insert(END, A_public[1])
def gen_key_prive():
	#A_prive,A_public = gen()
	entryK0.config(state=NORMAL)
	entryK0.insert(END, A_prive[0])
	entryK1.config(state=NORMAL)
	entryK1.insert(END, A_prive[1])

def efface():
	entryK0.delete(0,END)
	entryK1.delete(0,END)

def Signateur_rsa():
	global signe
	k0 = int(entryK0_P2.get(),10)
	k1 = int(entryK1_P2.get(),10)
	Message = entryMessage_P2.get()
	signe = tp2.rsa_sign(Message,(k0,k1))
	lblResult["text"]= "Signateur = "+ str(signe)
	entryMessage_P2.config(state=DISABLED)

def Verifie_rsa():
	entryMessage_P2.config(state=NORMAL)
	k0 = int(entryK0_P2.get(),10)
	k1 = int(entryK1_P2.get(),10)
	lblResult["text"]= "Vérifie Signateur = "+ str(tp2.rsa_verify(signe,(k0,k1)))
	
def gen_key_Public_P2():
	#A_prive,A_public = gen()
	entryK0_P2.config(state=NORMAL)
	entryK0_P2.insert(END, A_public[0])
	entryK1_P2.config(state=NORMAL)
	entryK1_P2.insert(END, A_public[1])
def gen_key_prive_P2():
	#A_prive,A_public = gen()
	entryK0_P2.config(state=NORMAL)
	entryK0_P2.insert(END, A_prive[0])
	entryK1_P2.config(state=NORMAL)
	entryK1_P2.insert(END, A_prive[1])	
def efface_P2():
	entryK0_P2.delete(0,END)
	entryK1_P2.delete(0,END)



if __name__ == '__main__':
	app = Tk() 
	app.title('APP Chiffrement Déchiffrement RSA <AIT EL DJOUDI Karim>')
	app.geometry('940x780')
	rows = 0
	while rows < 50:
	    app.rowconfigure(rows, weight=1)
	    app.columnconfigure(rows, weight=1)
	    rows += 1

	signe = None
	nb = ttk.Notebook(app)
	nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

	page1 = ttk.Frame(nb)
	nb.add(page1, text='ENC_RSA & DEC_RSA')

	labelbits = Label(page1,text = "Sur Combien de bits vous voulais Générer la clef")
	labelbits.grid(column=1, row=0, ipadx=0, pady=0, sticky=W+S)
	entrybits = Entry(page1, width=5)
	entrybits.grid(column=1, row=1, padx=10, pady=0, sticky=N)


	labelMessage = Label(page1,text = "Saisie votre Message")
	labelMessage.grid(column=0, row=4, ipadx=5, pady=14, sticky=W+N)

	labelk0 = Label(page1,text = "Générer cle_Public[0] Ou cle_Prive[0] (?, ) : ")
	labelk0.grid(column=0, row=2, ipadx=5, pady=0, sticky=W+S)

	labelk1 = Label(page1,text = "Générer cle_Public[1] Ou cle_Prive[1] ( ,?): ")
	labelk1.grid(column=0, row=3, ipadx=5, pady=0, sticky=W+S)


	entryMessage = Entry(page1, width=20)
	entryK0 = Entry(page1, width=20,state=DISABLED)
	entryK1 = Entry(page1, width=20,state=DISABLED)
	entryenc = Entry(page1,width=20,state=DISABLED)
	entryMessage.grid(column=1, row=4, padx=10, pady=12, sticky=N)
	entryK0.grid(column=1, row=2, padx=10, pady=0, sticky=S)
	entryK1.grid(column=1, row=3, padx=10, pady=0, sticky=S)

	btnGeer_public = Button(page1, text='clef Public', bg='yellow', fg='blue',command=gen_key_Public)
	btnGeer_public.grid(column=2, row=2,padx=74, pady=3,sticky=N)
	btnGeer_prive = Button(page1, text='celf Prive', bg='yellow', fg='blue',command=gen_key_prive)
	btnGeer_prive.grid(column=2, row=3,padx=74, pady=3,sticky=N)

	btnGeer_efface = Button(page1, text='sup', bg='yellow', fg='blue',command=efface)
	btnGeer_efface.grid(column=2, row=4,padx=74, pady=3,sticky=N)#

	resultButton_enc = Button(page1, text = 'ENC_RSA',command=affiche_enc)
	resultButton_enc.grid(column=0,padx=75,row=6, pady=45, sticky=W)

	resultButton_dec = Button(page1, text = 'DEC_RSA',command=affiche_dec)
	resultButton_dec.grid(column=0,padx=75,row=7, pady=0, sticky=W)

	lblResult_enc = Label(page1,fg="red")
	lblResult_enc.place(x =100, y = 255)
	
	page2 = ttk.Frame(nb)
	nb.add(page2, text='Signateur rsa & Vérifie')
	
	labelbits_P2 = Label(page2,text = "Sur Combien de bits vous voulais Générer la clef")
	labelbits_P2.grid(column=1, row=0, ipadx=0, pady=0, sticky=W+S)
	entrybits_P2 = Entry(page2, width=5)
	entrybits_P2.grid(column=1, row=1, padx=10, pady=0, sticky=N)


	labelMessage_P2 = Label(page2,text = "Saisie votre Message")
	labelMessage_P2.grid(column=0, row=4, ipadx=5, pady=14, sticky=W+N)

	labelk0_p2 = Label(page2,text = "Générer cle_Public[0] Ou cle_Prive[0] (?, ) : ")
	labelk0_p2.grid(column=0, row=2, ipadx=5, pady=0, sticky=W+S)

	labelk1_p2 = Label(page2,text = "Générer cle_Public[1] Ou cle_Prive[1] ( ,?): ")
	labelk1_p2.grid(column=0, row=3, ipadx=5, pady=0, sticky=W+S)


	entryMessage_P2 = Entry(page2, width=20)
	entryK0_P2 = Entry(page2, width=20,state=DISABLED)
	entryK1_P2 = Entry(page2, width=20,state=DISABLED)
	entrySign = Entry(page2,width=20,state=DISABLED)
	entryMessage_P2.grid(column=1, row=4, padx=10, pady=12, sticky=N)
	entryK0_P2.grid(column=1, row=2, padx=10, pady=0, sticky=S)
	entryK1_P2.grid(column=1, row=3, padx=10, pady=0, sticky=S)

	btnGeer_public_P2 = Button(page2, text='clef Public', bg='yellow', fg='blue',command=gen_key_Public_P2)
	btnGeer_public_P2.grid(column=2, row=2,padx=74, pady=3,sticky=N)

	btnGeer_prive_P2 = Button(page2, text='celf Prive', bg='yellow', fg='blue',command=gen_key_prive_P2)
	btnGeer_prive_P2.grid(column=2, row=3,padx=74, pady=3,sticky=N)

	btnGeer_efface_P2 = Button(page2, text='sup', bg='yellow', fg='blue',command=efface_P2)
	btnGeer_efface_P2.grid(column=2, row=4,padx=74, pady=3,sticky=N)#

	resultButton_sign = Button(page2, text = 'Signateur',command=Signateur_rsa)
	resultButton_sign.grid(column=0,padx=75,row=6, pady=45, sticky=W)

	resultButton_check = Button(page2, text = 'Vérifie',command=Verifie_rsa)
	resultButton_check.grid(column=0,padx=75,row=7, pady=0, sticky=W)


	lblResult = Label(page2,fg="red")
	lblResult.place(x = 100 , y = 255)



	app.mainloop()

from tkinter import * 
from tkinter import filedialog 
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os,random,struct,sys ,string,os.path
from termcolor import colored ,cprint
from tkinter import messagebox 
from PIL import ImageTk
from PIL import Image 
from Crypto.Cipher import AES 
import tp1 , enc_Image
format = "BMP" 
def action(event):
    select = listeCombo.get() 
    m = str(form_texte.get())
    n = int(form_k0.get(),10)
    l = int(form_k1.get(),10)
    if(select == "ENC"):
        lblResult['text'] = "ENC = "  + str(tp1.enc_byte(m,(n,l)))
    else:
        lblResult['text'] = "DEC   = " + tp1.dec_byte(int(tp1.enc_byte(m,(n,l))),(n,l))
def my_file(): 
    filename = askopenfilename(title="Ouvriaction(event):r votre document",filetypes=[('txt files','.txt'),('enc files','.enc'),('dec files','.dec'),('all files','.*')])
    fichier = open(filename,"r")
    content = fichier.read()
    fichier.close()
    Canvas(page2, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =190, pady =280)
    myLabel = Label(page2, text=content).grid(row =400, column =0, padx =190, pady =280)

def my_file3(): 
    filename = askopenfilename(title="Ouvriaction(event):r votre document",filetypes=[('dec files','.dec'),('enc files','.enc'),('all files','.*')])
    fichier = open(filename,"r")
    content = fichier.read()
    fichier.close()
    Canvas(page3, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =190, pady =280)
    myLabel = Label(page3, text=content).grid(row =400, column =0, padx =190, pady =280)

def myDelete():
    msg = messagebox.askyesnocancel('Info','Delete canevas ?')
    if msg == None :
        return
    elif msg == True :
        myLabel.pack_forget() 
def aide():
    messagebox.showinfo('Aide','malheureusement je peux pas vous aider !')

def petitFormat():
    main.geometry('640x480')
def formatNormal():
    main.geometry('840x680')
def grandFormat():
    main.geometry('1024x880')

def enc_filee(act):
    iv = 10
    enc = []
    int_k0 = int(p2_form_k0.get(),10)
    int_k1 = int(p2_form_k1.get(),10)
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])     
    file0 = open(filename,"r")
    file1 = open(filename+".enc","w")
    if(listeCombo2.get() == "ENC_MODE_ECB"):

        while True: 
            text = file0.read(1)
            if not text:
                break
            encF = tp1.enc_byte(text,(int_k0,int_k1))
            file1.write(chr(encF))
            enc.append(chr(encF))
        seq = enc
        text=("".join(seq))
        Canvas(page2, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text=text).grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text='voici le texte chiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close()
    if(listeCombo2.get() == "ENC_MODE_CBC"):
        while True: 
            text = file0.read(1)
            if not text:
                break
            xor_v_t = iv ^ ord(text)
            encF = tp1.enc_byte_cbs(xor_v_t, (int_k0,int_k1))
            iv = encF
            file1.write(chr(encF))
            enc.append(chr(encF))
        seq=enc 
        text=("".join(seq))
        Canvas(page2, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text=text).grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text='voici le texte chiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close() 

    if(listeCombo2.get() == "ENC_MODE_CFB"):
        while True: 
            text = file0.read(1)
            if not text:
                break
            encF = tp1.enc_byte_cbs(iv, (int_k0,int_k1))
            xor_v_t = ord(text) ^ encF
            iv = xor_v_t
            file1.write(chr(xor_v_t))
            enc.append(chr(xor_v_t))
        seq = enc
        text=("".join(seq))
        Canvas(page2, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text=text).grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text='voici le texte chiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close() 

    if(listeCombo2.get() == "ENC_MODE_OFB"):
        while True: 
            text = file0.read(1)
            if not text:
                break
            encF = tp1.enc_byte_cbs(iv,(int_k0,int_k1))
            iv = encF
            xor_v_t = ord(text) ^ encF
            file1.write(chr(xor_v_t))
            enc.append(chr(xor_v_t))
        seq = enc
        text=("".join(seq))
        Canvas(page2, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text=text).grid(row =400, column =0, padx =150, pady =280)
        myLabel = Label(page2, text='voici le texte chiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close()   

def dec_filee(acte):
    iv = 10
    dec = []
    int_k0 = int(p3_form_k0.get(),10)
    int_k1 = int(p3_form_k1.get(),10)
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('enc files','.enc'),('all files','.*')])     
    file0 = open(filename,"r")
    file1 = open(filename+".dec","w")
    if(listeCombo3.get() == "DEC_MODE_ECB"):  
        while True: 
            text0 = file0.read(1)
            if not text0:
                break
            encF = tp1.dec_byte(ord(text0),(int_k0,int_k1))
            file1.write(str(encF))
            dec.append(str(encF))
        seq = dec
        text=("".join(seq))
        Canvas(page3, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =180, pady =280)
        myLabel= Label(page3, text=text).grid(row =400, column =0, padx =180, pady =280)
        myLabel= Label(page3, text='voici le texte dechiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close()
    if(listeCombo3.get() == "DEC_MODE_CBC"):  
        while True: 
            text0 = file0.read(1)
            if not text0:
                break
            encF = tp1.dec_byte(ord(text0),(int_k0,int_k1))
            text_enc = ord(encF) ^ iv
            iv = ord(text0)
            file1.write(chr(text_enc))
            dec.append(chr(text_enc))
        seq = dec 
        text=("".join(seq))
        Canvas(page3, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =180, pady =280)
        myLabel = Label(page3, text=text).grid(row =400, column =0, padx =180, pady =280)
        myLabel = Label(page3, text='voici le texte dechiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close() 

    if(listeCombo3.get() == "DEC_MODE_CFB"):
        file = file0.read()
        for text0 in file: 
            encF = tp1.enc_byte_cbs(iv,(int_k0,int_k1))
            text_enc = encF ^ ord(text0);
            iv = ord(text0)
            file1.write(chr(text_enc))
            dec.append(chr(text_enc))
        seq = dec 
        text=("".join(seq))
        Canvas(page3, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =180, pady =280)
        myLabel = Label(page3, text=text).grid(row =400, column =0, padx =180, pady =280)
        myLabel = Label(page3, text='voici le texte dechiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close() 

    if(listeCombo3.get() == "DEC_MODE_OFB"):  
        while True: 
            text = file0.read(1)
            if not text:
                break
            encF = tp1.enc_byte_cbs(iv, (int_k0,int_k1))
            iv = encF
            xor_v_t = ord(text) ^ encF
            file1.write(chr(xor_v_t))
            dec.append(chr(xor_v_t))
        seq = dec
        text=("".join(seq))
        Canvas(page3, width=250, height=50, bg='ivory').grid(row =400, column =0, padx =190, pady =280)
        myLabel=Label(page3, text=text).grid(row =400, column =0, padx =180, pady =280)
        myLabel=Label(page3, text='voici le texte dechiffrer :').grid(row =400,sticky=W)
        file0.close()
        file1.close()   
def gen_key():
    key = enc_Image.gen_key(16)
    form_key_P4.config(state=NORMAL)
    form_key_P4.insert(END, key)
def efface():
    form_key_P4.delete(0,END)
   
def Ouvrir_img(event):
    key=form_key_P4.get()
    select = listeCombo_P4.get() 
    if len(key)<16 : 
        messagebox.showinfo('Info',"la longueur de la clef il faut qu'elle soit strictement égale a 16 caractère ou nombre si vous avez la flemme d'écrire vous avez qu'a cliquer sur le bouton a coté !")
    if select =="ENC_IMG_ECB":
        filepath = askopenfilename(title="Ouvrir une image",filetypes=[('bmp files','.bmp'),('png files','.png')])
        im = Image.open(filepath) 
        data = im.convert("RGB").tobytes()  
        original = len(data)
        new = enc_Image.Convertir_img(enc_Image.enc_ecb_encrypt(key,enc_Image.pad(data))[:original])   
        im2 = Image.new(im.mode, im.size) 
        im2.putdata(new) 
        im2.save(filepath+".ECB",format)
        messagebox.showinfo('Nickel',"Maintenant il vous reste qu'a regarder dans le fichier et vous trouvez l'image que vous avez chiffrer merci a bientôt")  
    if select =="ENC_IMG_CBC":
        filepath = askopenfilename(title="Ouvrir une image",filetypes=[('bmp files','.bmp'),('png files','.png')])
        im = Image.open(filepath) 
        data = im.convert("RGB").tobytes()  
        original = len(data)
        new = enc_Image.Convertir_img(enc_Image.enc_cbc_encrypt(key,enc_Image.pad(data))[:original])   
        im2 = Image.new(im.mode, im.size) 
        im2.putdata(new) 
        im2.save(filepath+".CBC",format)
        messagebox.showinfo('Nickel',"Maintenant il vous reste qu'a regarder dans le fichier et vous trouvez l'image que vous avez chiffrer merci a bientôt")   
if __name__ == '__main__':
    main = Tk()
    main.title('APP Chiffrement Par Bloc <AIT EL DJOUDI Karim>')
    main.geometry('840x680')
    myLabel = Label(main) 
    rows = 0
    while rows < 50:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1
    #------------------------------------------------ page1 --------------------------------------------------------------------
    nb = ttk.Notebook(main)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
    page1 = ttk.Frame(nb)
    nb.add(page1, text='enc_dec_lettre')

    texte_question = Label(page1, text='Entrez une lettre :')
    texte_question.grid(row =1, column =1, padx =1, pady =6)

    form_texte = Entry(page1, textvariable=StringVar())
    form_texte.grid(row =1, column =6, padx =3, pady =0)

    k0 = Label(page1, text='Entrez votre clef k[0] :')
    k0.grid(row =2, column =1, padx =1, pady =6)

    form_k0 = Entry(page1, textvariable=StringVar())
    form_k0.grid(row =2, column =6, padx =3, pady =0)

    k1 = Label(page1, text='Entrez votre clef k[1] :')
    k1.grid(row =3, column =1, padx =1, pady =6)
    form_k1 = Entry(page1, textvariable=StringVar())
    form_k1.grid(row =3, column =6, padx =3, pady =0)
    texte_combo = Label(page1, text='choisie :')
    texte_combo.grid(row =10, column =1, padx =1, pady =13)
    listeCombo = ttk.Combobox(page1, values=[ "ENC" , "DEC" ] )
    listeCombo.place(x = 155 , y = 110 , width = 165)
    listeCombo.bind("<<ComboboxSelected>>",action)
    lblResult = Label(page1 , text ="Result :  ")
    lblResult.place(x = 150 , y = 145)
    #-------------------------------------------------------- page 2 -------------------------------------
    page2 = ttk.Frame(nb)
    nb.add(page2, text='enc_file')
    zoneMenu = Frame(page2, borderwidth=3, bg='#557788')
    zoneMenu.grid(row=0,column=0)
    menuFichier = Menubutton(zoneMenu, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuFichier.grid(row=0,column=0)
    menuEdit = Menubutton(zoneMenu, text='Affichage', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuEdit.grid(row=0,column=1)
    menuActeul = Menubutton(zoneMenu, text='Actualiser', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuActeul.grid(row=0,column=3)
    menuDeroulant1 = Menu(menuFichier, tearoff = 0)
    menuDeroulant1.add_command(label="Ouvrir",command=my_file)
    menuDeroulant1.add_command(label="aide",command=aide)
    menuDeroulant_2 = Menu(menuActeul, tearoff = 0)
    menuDeroulant_2.add_command(label="Actualiser")
    menuDeroulant = Menu(menuEdit, tearoff = 0)
    menuDeroulant.add_command(label='Petit Format', command = petitFormat)
    menuDeroulant.add_command(label="Moyen Format", command = formatNormal)
    menuDeroulant.add_command(label="Grand Format", command = grandFormat)
    menuEdit.configure(menu=menuDeroulant)
    menuFichier.configure(menu=menuDeroulant1)
    menuActeul.configure(menu=menuDeroulant_2)
    p2_k0 = Label(page2, text='Entrez votre clef k[0] :')
    p2_k0.grid(row=2,sticky=W)
    p2_form_k0 = Entry(page2, textvariable=StringVar())
    p2_form_k0.grid(row =2, column =0, padx =0, pady =20)

    p2_k1 = Label(page2, text='Entrez votre clef k[1] :')
    p2_k1.grid(row =3, sticky=W)
    p2_form_k1 = Entry(page2, textvariable=StringVar())
    p2_form_k1.grid(row =3, column =0, padx =0, pady =0)
    texte_combo2 = Label(page2, text='choisie Mode chiffrement :')
    texte_combo2.grid(row =17,sticky=W,padx =0, pady =25)
    listeCombo2 = ttk.Combobox(page2, values=["ENC_MODE_ECB" ,"ENC_MODE_CBC" ,"ENC_MODE_CFB" ,"ENC_MODE_OFB"] )
    listeCombo2.place(x = 180 , y = 145 , width = 165)
    listeCombo2.bind("<<ComboboxSelected>>",enc_filee)

    #------------------------------------------------------------------- page3 ------------------------------------------------
    page3 = ttk.Frame(nb)
    nb.add(page3, text='dec_file')
    zoneMenu1 = Frame(page3, borderwidth=3, bg='#557788')
    zoneMenu1.grid(row=0,column=0)
    menuFichier1 = Menubutton(zoneMenu1, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuFichier1.grid(row=0,column=0)
    menuEdit1 = Menubutton(zoneMenu1, text='Affichage', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuEdit1.grid(row=0,column=1)
    menuActeul1 = Menubutton(zoneMenu1, text='Actualiser', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuActeul1.grid(row=0,column=3)
    menuDeroulant2 = Menu(menuFichier1, tearoff = 0)
    menuDeroulant2.add_command(label="Ouvrir",command=my_file3)
    menuDeroulant2.add_command(label="aide",command=aide)
    menuDeroulant_1 = Menu(menuActeul1, tearoff = 0)
    menuDeroulant_1.add_command(label="Actualiser",command=myLabel.grid_forget())
    menuDeroulant_3 = Menu(menuEdit1, tearoff = 0)
    menuDeroulant_3.add_command(label='Petit Format', command = petitFormat)
    menuDeroulant_3.add_command(label="Moyen Format", command = formatNormal)
    menuDeroulant_3.add_command(label="Grand Format", command = grandFormat)
    menuEdit1.configure(menu=menuDeroulant_3)
    menuFichier1.configure(menu=menuDeroulant2)
    menuActeul1.configure(menu=menuDeroulant_1)
    p3_k0 = Label(page3, text='Entrez votre clef k[0] :')
    p3_k0.grid(row=2,sticky=W)
    p3_form_k0 = Entry(page3, textvariable=StringVar())
    p3_form_k0.grid(row =2, column =0, padx =0, pady =20)

    p3_k1 = Label(page3, text='Entrez votre clef k[1] :')
    p3_k1.grid(row =3, sticky=W)
    p3_form_k1 = Entry(page3, textvariable=StringVar())
    p3_form_k1.grid(row =3, column =0, padx =0, pady =0)
    texte_combo3 = Label(page3, text='choisie Mode Dechiffrement:')
    texte_combo3.grid(row =17,sticky=W,padx =0, pady =25)
    listeCombo3 = ttk.Combobox(page3, values=["DEC_MODE_ECB" ,"DEC_MODE_CBC" ,"DEC_MODE_CFB" ,"DEC_MODE_OFB"] )
    listeCombo3.place(x = 195 , y = 145 , width = 165)
    listeCombo3.bind("<<ComboboxSelected>>",dec_filee)
#--------------------------------------- page 4 ------------------------------------------------------
    
    page4 = ttk.Frame(nb)
    nb.add(page4, text='chiffrer une Image')
    texte_question_P4 = Label(page4, text='Entrez une clef de len(16)  :')
    texte_question_P4.grid(row =1, column =0, padx =1, pady =6,sticky=W)

    form_key_P4 = Entry(page4, textvariable=StringVar())
    form_key_P4.grid(row =1, column =1, padx =3, pady =8,sticky=W)

    texte_combo_P4 = Label(page4, text='choisie le Mode de chiffrement :')
    texte_combo_P4.grid(row =2, column =0, padx =0, pady =6,sticky=W)
    listeCombo_P4 = ttk.Combobox(page4, values=[ "ENC_IMG_ECB" , "ENC_IMG_CBC" ] )
    listeCombo_P4.place(x = 216 , y = 85 , width = 165)
    listeCombo_P4.bind("<<ComboboxSelected>>",Ouvrir_img)
    
    resultButton_P4 = Button(page4,bg='yellow',fg='red', text = '>',command=gen_key)
    resultButton_P4.grid(column=3,row=1,padx=15, pady=25,sticky=W)
    
    btnGeer_efface_P4 = Button(page4, text='sup', bg='yellow', fg='red',command=efface)
    btnGeer_efface_P4.grid(column=4, row=1,padx=15, pady=25,sticky=N)#

    main.mainloop()

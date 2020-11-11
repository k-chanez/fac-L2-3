import os, random, struct
from termcolor import colored ,cprint 
import sys
import os.path
import string
"""--------------------------------------- Exercice 1 -------------------------------------------------------------------------------------"""
s = [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
def round(m, k):
	#x=k^m 
	return s[m^k]

def enc(m, key):
	t0 = round(m, key[0])
	t1 = round(t0, key[1])
	return t1

xobs = [s.index(i) for i in range(0,16)]

def back_round(c,k):
	return xobs[c]^k

def dec(c,k):
	a0 = back_round(c,k[1])
	a1 = back_round(a0,k[0])
	return a1 
"""--------------------------------------- Exercice 2 -------------------------------------------------------------------------------------"""
def enc_byte(oct,key):
	p=ord(oct)
	g,d= p>>4,p&0x0F
	s = enc(g,key)
	m = enc(d,key)
	rus = ((s<<4)+m)
	return rus
def dec_byte(oct,key):
	g,d= oct>>4,oct&0x0F
	s = dec(g,key)
	m = dec(d,key)
	rs= ((s<<4)+m)
	return chr(rs)

def bin_dec(bin):
    return int(bin,10)

def enc_file(file,key):
	enc = []
	file0 =open(file,"r")
	file1 = open(file+".enc","w")
	while True:	
		text = file0.read(1)
		if not text:
			break
		encF = enc_byte(text,key)
		file1.write(chr(encF))
		enc.append(chr(encF))
	seq = enc
	print("voici le résultat de chiffrement =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def dec_file(file,key):
	dec = []
	file0 = open(file,"r")
	file1 = open(file+".dec","w")
	while True:	
		text0 = file0.read(1)
		if not text0:
			break
		encF = dec_byte(ord(text0),key)
		file1.write(str(encF))
		dec.append(str(encF))
	seq = dec
	print("voici le résultat de déchiffrement =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()
"""--------------------------------------- Exercice 3 -------------------------------------------------------------------------------------"""
def enc_byte_cbs(p,key):
	g,d= p>>4,p&0x0F
	s = enc(g,key)
	m = enc(d,key)
	rus = ((s<<4)+m)
	return rus

def enc_file_cbc(file, key, iv):
	enc_cbc =[]
	file0 =open(file,"r")
	file1 = open(file+".enc","w")
	while True:	
		text = file0.read(1)
		if not text:
			break
		xor_v_t = iv ^ ord(text)
		encF = enc_byte_cbs(xor_v_t, key)
		iv = encF
		file1.write(chr(encF))
		enc_cbc.append(chr(encF))
	seq = enc_cbc
	print("voici le résultat de chiffrement CBC =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def dec_file_cbc(file,key, iv):
	dec_cbc = []
	file0 = open(file,"r")
	file1 = open(file+".dec","w")
	while True:	
		text0 = file0.read(1)
		if not text0:
			break
		encF = dec_byte(ord(text0),key)
		text_enc = ord(encF) ^ iv
		iv = ord(text0)
		file1.write(chr(text_enc))
		dec_cbc.append(chr(text_enc))
	seq = dec_cbc
	print("voici le résultat de déchiffrement CBC =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def enc_file_cfb(file, key, iv):
	enc_cfb = []
	file0 =open(file,"r")
	file1 = open(file+".enc","w")
	while True:	
		text = file0.read(1)
		if not text:
			break
		encF = enc_byte_cbs(iv, key)
		xor_v_t = ord(text) ^ encF
		iv = xor_v_t
		file1.write(chr(xor_v_t))
		enc_cfb.append(chr(xor_v_t))
	seq = enc_cfb
	print("voici le résultat de chiffrement CFB =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def dec_file_cfb(file,key, iv):
	dec_cfb = []
	file0 = open(file,"r")
	file1 = open(file+".dec","w") 
	while True:
		text0 = file0.read(1)
		if not text0:
			break
		encF = enc_byte_cbs(iv,key)
		text_enc = encF ^ ord(text0);
		iv = ord(text0)
		file1.write(chr(text_enc))
		dec_cfb.append(chr(text_enc))
	seq = dec_cfb
	print("voici le résultat de déchiffrement CFB =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def enc_file_ofb(file,key,iv):
	enc_ofb = []
	file0 = open(file,"r")
	file1 = open(file+".enc","w")
	while True:	
		text = file0.read(1)
		if not text:
			break
		encF = enc_byte_cbs(iv, key)
		iv = encF
		xor_v_t = ord(text) ^ encF
		file1.write(chr(xor_v_t))
		enc_ofb.append(chr(xor_v_t))
	seq = enc_ofb
	print("voici le résultat de déchiffrement OFB =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()

def dec_file_ofb(file,key, iv):
	dec_ofb = []
	file0 = open(file,"r")
	file1 = open(file+".dec","w") 
	while True:
		text0 = file0.read(1)
		if not text0:
			break
		encF = enc_byte_cbs(iv,key)
		text_enc = ord(text0) ^ encF;
		iv = encF
		file1.write(chr(text_enc))
		dec_ofb.append(chr(text_enc))
	seq = dec_ofb
	print("voici le résultat de déchiffrement OFB =>",colored("".join(seq),'red'))
	file0.close()
	file1.close()
	



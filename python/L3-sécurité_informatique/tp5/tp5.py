from Crypto.Util.number import getPrime, inverse 
from math import gcd
import os ,ssl, socket,random
from time import time 
"""----------------------------------------- Exercice 1 ------------------------------------------------------------------------------- """

def rsa_CRT_key_prive(p,q,d):
	dp = d % (p - 1)
	dq = d % (q - 1)
	iq = inverse(q,p)
	return dp,dq,iq
	
def signe_rsa_crt(msg,dp,dq,p,q,iq):
	sp=pow(msg,dp,p)
	sq=pow(msg,dq,q)
	sCRT = sq+q*(iq*(sp-sq)%p)
	return sCRT

def benchmark_rsa(msg,d,n):
	beg = time()
	for i in range(1000):
		s = pow(msg,d,n)
	end = time()
	temps =(end - beg)
	return temps

def benchmark_rsa_CRT(p,q,d):
	beg = time()
	msg = random.getrandbits(64)
	dp, dq, iq = rsa_CRT_key_prive(p,q,d)
	for i in range(1000):
		signe_rsa_crt(msg, dp, dq, p, q, iq)
	end = time()
	temps =(end - beg)
	return temps


"""----------------------------------------- Exercice 2 ------------------------------------------------------------------------------- """

def injecter_fautes(msg,dp,dq,p,q,iq):
	sp=pow(msg,dp,p)-1
	sq=pow(msg,dq,q)
	sCRT= sq+q*(iq*(sp+sq)%p)
	return sCRT

def trouve_p_q(s, sfaux, N):
	q = gcd(N, (s - sfaux))
	p = N // q
	return p,q

def trouve_d(e, p, q):
	phi_N = (p - 1) * (q - 1)
	d = inverse(e,phi_N)
	return d

def retrouve_message(N, e, d, p, q):
	msg = random.getrandbits(64)
	dp, dq, iq = rsa_CRT_key_prive(p, q, d)
	scrt = signe_rsa_crt(msg,dp,dq,p,q,iq)
	print("message_origine =>",msg)
	print("signateur =>",scrt)
	message = pow(scrt, e, N)
	print("message_trouve =>",message)

def envoye_une_attaque(msg,d,n):
	return pow(msg,d,n)

def main():
	bits=1024
	p = getPrime(512)
	q = getPrime(515)
	n = p*q
	phi_n = (p-1)*(q-1)
	e= 65537
	assert(gcd(e,phi_n))
	d = inverse(e,phi_n)
	rsa_calasique = ((e,n),(d,n))
	dp , dq, iq = rsa_CRT_key_prive(p,q,d)
	msg=random.getrandbits(64)
	temps1 = benchmark_rsa(msg,d,n)
	print("le temps signe_rsa_calasique =>",temps1)
	temps2 = benchmark_rsa_CRT(p,q,d)
	print("le temps signe_rsa_crt =>",temps2)
	print("facteur de vitesse gagner par l’optimisation CRT =>",temps1 - temps2)
	s_vrai =0x3f010be37eb5eca9
	s_faux= 0x424a4dfd3625451d
	N = 47775493107113604137
	e = 17
	p,q =trouve_p_q(s_vrai, s_faux, N)
	print("(p,q) =>",(p,q))
	d = trouve_d(e,p,q)
	print("(d) =>",(d))
	retrouve_message(N,e,d,p,q)
	print("cle prive [p,q,dp,dq,iq] =>",[p,q,rsa_CRT_key_prive(p,q,d)])

main()
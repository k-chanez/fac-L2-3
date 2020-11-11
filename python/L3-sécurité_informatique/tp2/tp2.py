from Crypto.Util.number import getPrime, inverse 
from math import gcd 
import os 
import ssl, socket
import hashlib

"""---------------------------------------Exercice 1 -------------------------------------------------------------------------------------"""

def get_prime(bits):
	openssl = os.popen('openssl prime -generate -bits ' + str(bits))
	p = int(openssl.read())
	openssl.close()
	return p 

def gen_rsa_key(bits):
	p = get_prime(bits//2)
	q = get_prime(bits//2)
	n = p*q
	phi_n = (p-1)*(q-1)
	e= 65537
	assert(gcd(e,phi_n))
	d = inverse(e,phi_n)
	return((e,n),(d,n))


"""---------------------------------------Exercice 2 -------------------------------------------------------------------------------------"""

def rsa(msg,key):
	return pow(msg,key[0],key[1])

def rsa_enc(msg,key):
	octet = msg.encode('utf-8')
	secret=int.from_bytes(octet,'big')
	return rsa(secret,key);


def rsa_dec(msg,key):
	txt_clair = rsa(msg,key)
	return txt_clair.to_bytes((txt_clair.bit_length() + 7) // 8,'big').decode('utf-8')
'''
A_prive , A_public= gen_rsa_key(1024)
B_prive , B_public=gen_rsa_key(1024)
message ='karim'
print("le message c'est :",message)
enc = rsa_enc(message,A_public)
print("déchiffrer =>",rsa_dec(enc,A_prive))
'''
"""--------------------------------------- Exercice 3 -------------------------------------------------------------------------------------"""

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)

    return result 

# celle-la c'est la version que j'ai code apres avoir compirs le cours mais elle marche pas moins de 512 bits
def h_(entier): 
    hache = hashlib.sha256(entier.encode())
    return hache.hexdigest()

def rsa_sign_(m, key):
    hache = h_(m)
    msg = int.from_bytes(hache.encode('utf-8'),'big')
    return pow(msg, key[0],key[1])

def rsa_verify_(m, k, signe):
	message_hache = h_(m)
	msg = int.from_bytes(message_hache.encode('utf-8'),'big')
	signature = pow(signe,k[0],k[1])
	if msg == signature:
		return True
	else:
		return False
'''
message='tout vas bien'
message_signe=rsa_sign_(message,A_prive)
vrf=rsa_verify_(message,A_public,message_signe)
print("la signature =>",vrf)
'''
#celle-la c'est la version quand je suis bloque sur la premier je teste frachement ca marche mais je sais pas comment hhhhh!
def h(entier): 
	message_hache = hashlib.sha256(entier.encode('utf-8')).hexdigest()
	return int(message_hache,16)

def rsa_sign(m, key):
    signature = rsa(h(m), key)
    return (m,signature)

def rsa_verify(m, key):
	signature = rsa(m[1],key)
	if h(m[0]) == signature:
		return True
	else:
		return False
'''		
message='tout vas bien'
message_signe=rsa_sign_(message,A_public)
vrf=rsa_verify_(message_signe,A_prive)
print("la signature =>",vrf)
'''

'''
 j'ai implemente ca de puis le debut mais quand j'essaye avec deux clef pareil il
 me renvois pas False il renvois des erreurs 
def h(entier): 
	message_hache = hashlib.sha256(entier.encode())
	return message_hache.hexdigest()

def rsa_sign(m, key):
    message_hache = h(m);
    return rsa_enc(message_hache, key)
def rsa_verify(m, k, signe):
	signature = rsa_dec(signe,k)
	if h(m) == signature:
		return True
	else:
		return False
'''


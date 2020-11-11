from PIL import Image 
from Crypto.Cipher import AES 
import random
import string

"""
filename = "tux.bmp" 
filename_out = "tux_dec" 
format = "BMP" 
key = "0123456789a11213" 
"""
def gen_key(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))
#key = gen_key(16)    
def pad(data): 
    return data + b"\x00"*(16-len(data)%16)   
def Convertir_img(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 
     
def Ouvrir_image(filename):

    im = Image.open(filename) 
    data = im.convert("RGB").tobytes()  
    original = len(data)  
    new = Convertir_img(enc_cbc_encrypt(key,pad(data))[:original]) 
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new) 
    im2.save(filename_out+"."+format, format) 

def enc_cbc_encrypt(key, data, mode=AES.MODE_CBC): 
    IV = "A"*16
    img = AES.new(key, mode, IV) 
    new_data = img.encrypt(data) 
    return new_data 
def enc_ecb_encrypt(key, data, mode=AES.MODE_ECB): 
    img = AES.new(key, mode) 
    new_data = img.encrypt(data) 
    return new_data 
#Ouvrir_image(filename) 
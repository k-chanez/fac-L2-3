import random

sbox = [9, 11, 12, 4, 10, 1, 2, 6, 13, 7, 3, 8, 15, 14, 0, 5]
xbos = [14, 5, 6, 10, 3, 15, 7, 9, 11, 0, 4, 1, 2, 8, 13, 12]


"""----------------------------------------- Exercice 1 ------------------------------------------------------------------------------- """

def round(msg, subkey):
	return sbox[msg ^ subkey]

def enc(m, key):
    t = round(m,key[0])
    c = round(t,key[1])
    return c

def dec (c, key):
    t = xobs[c] ^ key[1]
    m = xobs[t] ^ key[0]
    return m

"""----------------------------------------- Exercice 2 ------------------------------------------------------------------------------- """

def generer_msg(size, key):
    size = max(size, 16)
    list_msg = []
    for i in range(0, size):
        list_msg.append((i, enc(i, key))) 
    return list_msg

"""----------------------------------------- Exercice 3 ----------------------------------------------------------------------------------""" 

def to_bits(number):
    return bin(number).count('1')

def calcule_parity():
    list_mask = []
    for mask_i in range(1, 16):
        for mask_o in range(1, 16):
            score = 0
            for i in range(0, 16):
                parity_i = to_bits(i & mask_i)
                parity_o = to_bits(sbox[i] & mask_o)
                if parity_i & 1 == parity_o & 1:
                    score += 1
            list_mask.append((mask_i, mask_o, score))

    return list_mask

def meilleure_paire(list_mask):
	best_mask = []
	find_best_mask = max(list_mask, key=lambda x: x[2])
	for (mask_i, mask_o, score) in list_mask:
		if score == find_best_mask[2]:
			best_mask.append((mask_i, mask_o, to_bits(mask_i), to_bits(mask_o)))
	return max(best_mask, key=lambda x: (x[2], x[3]))[0:2]

"""----------------------------------------- Exercice 4 ---------------------------------------------------------------------------------------"""

def k0(list_msg, mask_i, mask_o):
    list_k0 = []
    for k0 in range(0, 16):
        score_equal = 0
        score_notequal = 0
        for (msg, c) in list_msg:
            t = round(msg, k0)
            parity_i = to_bits(t & mask_i) & 1
            parity_o = to_bits(c & mask_o) & 1
            if parity_i == parity_o:
                score_equal += 1
            else:
                score_notequal += 1
            if score_equal > score_notequal:
                score = score_equal
            else:
                score = score_notequal
        list_k0.append((k0, score))
    max_ = max(list_k0, key=lambda x: x[1])
    return [key for (key, score) in list_k0 if
            score == max_[1]]
            
"""----------------------------------------- Exercice 5 --------------------------------------------------------------------"""

def k1(list_k0, list_msg):
    list_k1 = []
    m = random.randint(0, 15)
    msg = list_msg[m][0]
    c = list_msg[m][1]
    for k0 in list_k0:
        t = round(msg, k0)
        k1 = xbos[c] ^ t
        list_k1.append(k1)
    return list_k1


def attack_force_brute(list_msg, list_key):
    key = []
    for k in list_key:
        tmp = 0
        for (msg, c) in list_msg:
            if c != enc(msg, k):
                tmp = 1
                break
        if tmp == 0:
            key.append(k)
    if len(key) == 1:
        return key[0]
    else:
        return "pas de clef trouve"


initial_lb = (0,2)
but = (7,4)
lab=[[1,1,2,1,1,1,0,1,0,1,1,1],
	 [1,0,0,1,1,1,0,1,0,1,0,1],
	 [1,0,1,1,0,1,0,1,0,1,0,1],
	 [1,0,1,0,0,0,1,1,0,1,0,1],
	 [1,0,0,0,1,0,0,1,1,1,1,1],
	 [1,1,1,1,1,0,1,1,0,1,0,1],
	 [1,0,0,1,0,0,1,1,0,1,0,1],
	 [1,1,1,1,3,1,1,1,0,1,1,1]]
def successeurs(etat ,lb):
	depart=[etat[1],etat[0]]
	chemin = []
	
	if(depart[1] < len(lb)-1 and lb[depart[1]+1][depart[0]]!=1):#n
		chemin.append((depart[1] +1,depart[0]))

	if(depart[0] > 0 and lb[depart[1]][depart[0]-1]!=1):#o
		chemin.append((depart[1],depart[0] - 1))

	if(depart[1] > 0 and lb[depart[1]-1][depart[0]]!=1):#s
		chemin.append((depart[1]- 1, depart[0]))

	if(depart[0] < len(lb[0])-1 and lb[depart[1]][depart[0]+1]!=1):#e
		chemin.append((depart[1], depart[0] +1))
	return chemin


class Etat:
    def __init__(self, liste, h, nbr_coup, verfier):
        self.h = h
        self.nbr_coup = nbr_coup
        self.f = h+nbr_coup
        self.verfier = verfier
        self.liste = liste
def h(e):
	a = but[0]-e[0] 
	b = but[1]-e[1]
	return a*a + b*b
def petit_cout(f):
	indix = 0 

	for i in range (len(f)):
		if (f[indix].f > f[i].f):
			indix = i 
	return indix 

def A_etoil():
	e0 = Etat(initial_lb,h(initial_lb),0,None)
	F = []
	v = []
	F.append(e0)
	e = e0
	while(e.h > 0 and len(F)):
		e = F[petit_cout(F)]
		F.remove(e)
		v.append(e)
		for s in successeurs(e.liste,lab):
			F.append(Etat(s,h(s),e.nbr_coup+1,e))
	if (e.h == 0 ):
		l =[]
		while(e.verfier != None):
			l.insert(0,e.liste)
			e = e.verfier
		l.insert(0,e.liste)
		return l 
	else :
		return [] 
print("chemin de Labyrinth en A*")
[print(A) for A in A_etoil()]

def affichage_laby(l,sol):
	for y in range(len(l)):
		for x in range(len(l[y])):
			if(l[y][x] == 1): 
				print("#",end='')
			elif ( l[y][x] == 0 ):
				if (y,x) in sol :
					print ("@",end='') 
				
				else:				
					print(" ",end='')
			elif (l[y][x] == 2):
				print("D",end='')
			elif (l[y][x] == 3):
				print("F",end='')	
		print()
affichage_laby(lab,A_etoil())	

